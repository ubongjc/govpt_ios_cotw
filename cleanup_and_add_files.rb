#!/usr/bin/env ruby
require 'xcodeproj'

puts "🧹 Cleaning up and re-adding files to Xcode project..."
puts ""

project_path = 'GPT.xcodeproj'
project = Xcodeproj::Project.open(project_path)
target = project.targets.first

puts "Target: #{target.name}"
puts ""

# List of file basenames we're managing
file_basenames = [
  'DatabaseManager.swift',
  'Region.swift',
  'Officeholder.swift',
  'Promise.swift',
  'Evidence.swift',
  'StatusSnapshot.swift',
  'Industry.swift',
  'SearchService.swift',
  'GeoService.swift',
  'HomeMapView.swift',
  'CountryView.swift',
  'PromisesListView.swift',
  'PromiseDetailView.swift',
  'SearchView.swift'
]

# Step 1: Remove ALL references to these files from the build phase
puts "🗑️  Removing all existing references from build phase..."
files_to_remove = []
target.source_build_phase.files.each do |build_file|
  file_ref = build_file.file_ref
  next unless file_ref

  if file_basenames.include?(File.basename(file_ref.path.to_s))
    puts "   Removing from build: #{file_ref.path}"
    files_to_remove << build_file
  end
end

files_to_remove.each { |f| f.remove_from_project }
puts "   Removed #{files_to_remove.count} build file references"
puts ""

# Step 2: Remove ALL file references from the project tree
puts "🗑️  Removing all existing file references from project tree..."
refs_to_remove = []
project.main_group.recursive_children.each do |item|
  if item.is_a?(Xcodeproj::Project::Object::PBXFileReference)
    if file_basenames.include?(File.basename(item.path.to_s))
      puts "   Removing reference: #{item.path}"
      refs_to_remove << item
    end
  end
end

refs_to_remove.each { |r| r.remove_from_project }
puts "   Removed #{refs_to_remove.count} file references"
puts ""

# Step 3: Add files with correct paths
puts "✅ Adding files with correct paths..."

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

  # Add file reference with correct path
  file_ref = folder_group.new_reference(filename)
  file_ref.source_tree = '<group>'

  # Add to target
  target.add_file_references([file_ref])

  puts "   ✅ Added: #{folder}/#{filename}"
end

# Save project
project.save

puts ""
puts "=" * 60
puts "✅ COMPLETE! Project cleaned and files added correctly"
puts "=" * 60
puts ""
puts "🚀 Now build:"
puts "   xcodebuild -project GPT.xcodeproj -scheme GPT -sdk iphonesimulator build"
puts ""
