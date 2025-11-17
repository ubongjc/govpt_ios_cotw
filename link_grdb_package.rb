#!/usr/bin/env ruby
require 'xcodeproj'

puts "🔗 Linking GRDB package to target..."
puts ""

project_path = 'GPT.xcodeproj'
project = Xcodeproj::Project.open(project_path)
target = project.targets.first

puts "Target: #{target.name}"
puts ""

# Find the GRDB package product
grdb_package = nil
project.root_object.package_references.each do |package_ref|
  if package_ref.repositoryURL.include?('GRDB.swift')
    puts "✅ Found GRDB package: #{package_ref.repositoryURL}"
    grdb_package = package_ref
    break
  end
end

if grdb_package.nil?
  puts "❌ GRDB package not found in project!"
  puts "Adding GRDB package reference..."

  # Add package reference
  package_ref = project.root_object.new_package_reference(
    'https://github.com/groue/GRDB.swift',
    kind: 'branch',
    name: 'GRDB.swift'
  )

  grdb_package = package_ref
  puts "✅ Added GRDB package reference"
end

# Check if GRDB is already in the dependencies
already_linked = false
target.package_product_dependencies.each do |dep|
  if dep.product_name == 'GRDB'
    puts "⏭️  GRDB already linked to target"
    already_linked = true
    break
  end
end

unless already_linked
  # Find or create the GRDB product dependency
  grdb_product = nil

  # Look for existing GRDB product
  project.root_object.project_references.each do |ref|
    products_group = ref[:product_group]
    products_group.children.each do |product|
      if product.display_name =~ /GRDB/
        grdb_product = product
        break
      end
    end
    break if grdb_product
  end

  # If we can't find it, try adding it via package product dependency
  if grdb_product.nil?
    puts "Creating GRDB package product dependency..."
    grdb_product = project.new(Xcodeproj::Project::Object::XCSwiftPackageProductDependency)
    grdb_product.package = grdb_package
    grdb_product.product_name = 'GRDB'
  end

  # Add to target dependencies
  target.package_product_dependencies << grdb_product
  puts "✅ Linked GRDB to target"
end

# Also add to frameworks build phase if needed
frameworks_phase = target.frameworks_build_phase
grdb_in_frameworks = false

frameworks_phase.files.each do |file|
  if file.display_name =~ /GRDB/
    grdb_in_frameworks = true
    break
  end
end

unless grdb_in_frameworks
  puts "Adding GRDB to frameworks build phase..."
  # This is automatically handled by Xcode for SPM packages
  puts "✅ Will be added automatically by Xcode"
end

# Save project
project.save

puts ""
puts "=" * 60
puts "✅ COMPLETE! GRDB package linked to target"
puts "=" * 60
puts ""
puts "🚀 Now try building:"
puts "   xcodebuild -project GPT.xcodeproj -scheme GPT -sdk iphonesimulator build"
puts ""
