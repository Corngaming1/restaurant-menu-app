

def update_price(self, name, new_price):
  if name in self.menu_items:
    self.menu_items[name] = new_price
    return True
  return False
