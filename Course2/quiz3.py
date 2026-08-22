# invalid dictionary - this should break
# research_topics = {
#    ['AlexNet', 'Convolutional Neural Network']: 'Image Classification',
#    ['VGG', 'Visual Geometry Group']: 'Deep Learning',
#    ['ResNet', 'Residual Networks']: 'Network Architecture'
#}


# corrected dictionary using tuples as keys
research_topics = {
    ('AlexNet', 'Convolutional Neural Network'): 'Image Classification',
    ('VGG', 'Visual Geometry Group'): 'Deep Learning',
    ('ResNet', 'Residual Networks'): 'Network Architecture'
}

# Verify the corrected dictionary
print(research_topics)
