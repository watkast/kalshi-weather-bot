# Range-Scalp Bot

*Updated Sat Nov 21 02:46 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 66942 | 58427 | 8515 (128) | 4 | $-17970.40 | -4.3% |
| **+10¢** | 49988 | 40035 | 9953 (170) | 5 | $-16708.28 | -5.3% |
| **+15¢** | 41917 | 31186 | 10731 (217) | 5 | $-15005.89 | -5.7% |
| **+20¢** | 37309 | 26034 | 11275 (274) | 5 | $-13326.69 | -5.7% |
| **+10¢ (15¢ stop)** | 81498 | 81332 | 166 (100) | 2 | $-30023.13 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-21 02:46 | +10 stop | NEAR | UP | 0.63 | open |  |
| 11-21 02:46 | +20 | NEAR | UP | 0.63 | open |  |
| 11-21 02:46 | +15 | NEAR | UP | 0.63 | open |  |
| 11-21 02:46 | +10 | NEAR | UP | 0.63 | open |  |
| 11-21 02:46 | +5 | NEAR | UP | 0.63 | open |  |
| 11-21 02:46 | +10 | HYPE | UP | 0.71 | open |  |
| 11-21 02:46 | +5 | HYPE | UP | 0.71 | open |  |
| 11-21 02:46 | +10 stop | SOL | UP | 0.57 | 0.68 | 0.73 |
| 11-21 02:46 | +20 | SOL | UP | 0.57 | open |  |
| 11-21 02:46 | +15 | SOL | UP | 0.57 | open |  |
| 11-21 02:46 | +10 | SOL | UP | 0.57 | 0.68 | 0.73 |
| 11-21 02:46 | +5 | SOL | UP | 0.57 | 0.68 | 0.73 |
| 11-21 02:46 | +10 stop | DOGE | DOWN | 0.52 | 0.37 | -1.85 |
| 11-21 02:46 | +20 | DOGE | DOWN | 0.52 | open |  |
| 11-21 02:46 | +15 | DOGE | DOWN | 0.52 | open |  |
| 11-21 02:46 | +10 | DOGE | DOWN | 0.52 | open |  |
| 11-21 02:46 | +5 | DOGE | DOWN | 0.52 | 0.58 | 0.24 |
| 11-21 02:45 | +10 stop | ZEC | DOWN | 0.62 | open |  |
| 11-21 02:45 | +20 | ZEC | DOWN | 0.62 | open |  |
| 11-21 02:45 | +15 | ZEC | DOWN | 0.62 | open |  |
| 11-21 02:45 | +10 | ZEC | DOWN | 0.62 | open |  |
| 11-21 02:45 | +5 | ZEC | DOWN | 0.62 | open |  |
| 11-21 02:45 | +10 stop | ETH | DOWN | 0.61 | 0.42 | -2.25 |
| 11-21 02:45 | +20 | ETH | DOWN | 0.61 | open |  |
| 11-21 02:45 | +15 | ETH | DOWN | 0.61 | open |  |
| 11-21 02:45 | +10 | ETH | DOWN | 0.61 | open |  |
| 11-21 02:45 | +5 | ETH | DOWN | 0.61 | open |  |
| 11-21 02:32 | +5 | BTC | DOWN | 0.65 | 0.73 | 0.50 |
| 11-21 02:31 | +10 stop | SOL | DOWN | 0.70 | 0.83 | 1.05 |
| 11-21 02:31 | +20 | SOL | DOWN | 0.70 | 0.91 | 1.93 |
| 11-21 02:31 | +15 | SOL | DOWN | 0.70 | 0.89 | 1.68 |
| 11-21 02:31 | +10 | SOL | DOWN | 0.70 | 0.83 | 1.05 |
| 11-21 02:31 | +5 | SOL | DOWN | 0.70 | 0.79 | 0.63 |
| 11-21 02:31 | +10 stop | HYPE | DOWN | 0.59 | 0.69 | 0.68 |
| 11-21 02:31 | +20 | HYPE | DOWN | 0.59 | 0.84 | 2.23 |
| 11-21 02:31 | +15 | HYPE | DOWN | 0.59 | 0.76 | 1.40 |
| 11-21 02:31 | +10 | HYPE | DOWN | 0.59 | 0.69 | 0.68 |
| 11-21 02:31 | +5 | HYPE | DOWN | 0.59 | 0.65 | 0.27 |
| 11-21 02:31 | +10 stop | BTC | DOWN | 0.61 | 0.73 | 0.89 |
| 11-21 02:31 | +20 | BTC | DOWN | 0.61 | 0.86 | 2.24 |
