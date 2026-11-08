# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


def migrate(cr, version):
    """Time types were shared by all companies before: keep them shared
    instead of assigning them all to the company that runs the update."""
    cr.execute("UPDATE project_time_type SET company_id = NULL")
