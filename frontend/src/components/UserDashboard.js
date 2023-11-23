import React from 'react'

const UserDashboard = () => {
  return (
    <header className="p-4 dark:bg-gray-800 dark:text-gray-100">
	<div className="container flex justify-between h-16 mx-auto">
	<h1>UserDashboard</h1>
		
		<div className="flex items-center md:space-x-4">
			<button type="button" className="hidden px-6 py-2 font-semibold rounded lg:block dark:bg-violet-400 dark:text-gray-900">Log Out</button>
		</div>
	</div>
</header>
  )
}
export default UserDashboard;
