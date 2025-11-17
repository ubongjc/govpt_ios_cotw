#!/usr/bin/env ruby
require 'xcodeproj'

puts "🔧 Adding missing files to Xcode project..."
puts ""

project_path = 'GPT.xcodeproj'
project = Xcodeproj::Project.open(project_path)
target = project.targets.first

puts "Target: #{target.name}"
puts ""

# Files to add (relative to project root)
files_to_add = [
  'GPT/Database/DatabaseManager.swift',
  'GPT/Models/Region.swift',
  'GPT/Models/Officeholder.swift',
  'GPT/Models/Promise.swift',
  'GPT/Models/Evidence.swift',
  'GPT/Models/StatusSnapshot.swift',
  'GPT/Models/Industry.swift',
  'GPT/Services/SearchService.swift',
  'GPT/Services/GeoService.swift',
  'GPT/Views/HomeMapView.swift',
  'GPT/Views/CountryView.swift',
  'GPT/Views/PromisesListView.swift',
  'GPT/Views/PromiseDetailView.swift',
  'GPT/Views/SearchView.swift'
]

added_count = 0
skipped_count = 0

files_to_add.each do |file_path|
  # Check if file already in project
  file_ref = project.main_group.find_file_by_path(file_path)

  if file_ref && target.source_build_phase.files_references.include?(file_ref)
    puts "⏭️  Skipping: #{File.basename(file_path)} (already in target)"
    skipped_count += 1
  else
    # Add file reference if it doesn't exist
    if !file_ref
      # Navigate to correct group
      path_components = file_path.split('/')
      group = project.main_group

      # Create/find groups for path
      (0...path_components.length-1).each do |i|
        group_name = path_components[i]
        existing_group = group.children.find { |child| child.is_a?(Xcodeproj::Project::Object::PBXGroup) && child.display_name == group_name }

        if existing_group
          group = existing_group
        else
          group = group.new_group(group_name, group_name)
        end
      end

      # Add file to group
      file_ref = group.new_reference(file_path)
    end

    # Add to target
    target.add_file_references([file_ref])
    puts "✅ Added: #{File.basename(file_path)}"
    added_count += 1
  end
end

# Save project
project.save

puts ""
puts "=" * 60
puts "✅ COMPLETE!"
puts "=" * 60
puts "Added: #{added_count} files"
puts "Skipped: #{skipped_count} files (already in target)"
puts ""
puts "🚀 Now try building in Xcode:"
puts "   cd /Users/ubongjosiah/gpt_iphone"
puts "   open GPT.xcodeproj"
puts "   # Press ⌘B to build"
puts ""
