#!/usr/bin/env ruby
require 'xcodeproj'

puts "🔧 Fixing file paths in Xcode project..."
puts ""

project_path = 'GPT.xcodeproj'
project = Xcodeproj::Project.open(project_path)
target = project.targets.first

puts "Target: #{target.name}"
puts ""

# Remove all incorrectly added files
target.source_build_phase.files.each do |build_file|
  file_ref = build_file.file_ref
  next unless file_ref

  if file_ref.path && file_ref.path.include?('GPT/GPT/')
    puts "❌ Removing incorrectly added: #{file_ref.path}"
    build_file.remove_from_project
  end
end

# Also remove the file references
project.main_group.recursive_children.each do |item|
  if item.is_a?(Xcodeproj::Project::Object::PBXFileReference) && item.path && item.path.include?('GPT/GPT/')
    puts "🗑️  Removing bad reference: #{item.path}"
    item.remove_from_project
  end
end

# Now add files with correct paths
files_to_add = [
  'Database/DatabaseManager.swift',
  'Models/Region.swift',
  'Models/Officeholder.swift',
  'Models/Promise.swift',
  'Models/Evidence.swift',
  'Models/StatusSnapshot.swift',
  'Models/Industry.swift',
  'Services/SearchService.swift',
  'Services/GeoService.swift',
  'Views/HomeMapView.swift',
  'Views/CountryView.swift',
  'Views/PromisesListView.swift',
  'Views/PromiseDetailView.swift',
  'Views/SearchView.swift'
]

# Find the GPT group
gpt_group = project.main_group.children.find { |child| child.display_name == 'GPT' }

if !gpt_group
  puts "❌ Could not find GPT group!"
  exit 1
end

files_to_add.each do |file_path|
  path_components = file_path.split('/')
  folder = path_components[0]
  filename = path_components[1]

  # Find or create folder group
  folder_group = gpt_group.children.find { |child| child.display_name == folder }
  if !folder_group
    folder_group = gpt_group.new_group(folder, folder)
  end

  # Add file reference
  file_ref = folder_group.new_reference(filename)
  file_ref.source_tree = '<group>'

  # Add to target
  target.add_file_references([file_ref])

  puts "✅ Added: #{folder}/#{filename}"
end

# Save project
project.save

puts ""
puts "=" * 60
puts "✅ COMPLETE! File paths fixed"
puts "=" * 60
puts ""
puts "🚀 Now build in Xcode or run:"
puts "   xcodebuild -project GPT.xcodeproj -scheme GPT -sdk iphonesimulator build"
puts ""
