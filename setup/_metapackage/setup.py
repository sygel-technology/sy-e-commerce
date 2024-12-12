import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-sygel-technology-sy-e-commerce",
    description="Meta package for sygel-technology-sy-e-commerce Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-website_transfer_payment_mode>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
