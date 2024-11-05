import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-sygel-technology-sy-e-commerce",
    description="Meta package for sygel-technology-sy-e-commerce Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-website_transfer_payment_mode>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
