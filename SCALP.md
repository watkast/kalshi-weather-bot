# Range-Scalp Bot

*Updated Mon Oct 12 16:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 13628 | 11796 | 1832 (25) | 1 | $-4313.49 | -5.0% |
| **+10¢** | 10322 | 8195 | 2127 (37) | 1 | $-4026.10 | -6.2% |
| **+15¢** | 8679 | 6404 | 2275 (55) | 1 | $-3558.32 | -6.5% |
| **+20¢** | 7725 | 5351 | 2374 (70) | 1 | $-3038.39 | -6.3% |
| **+10¢ (15¢ stop)** | 16752 | 16705 | 47 (27) | 0 | $-6559.00 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-12 16:48 | +10 stop | SOL | UP | 0.58 | 0.31 | -3.03 |
| 10-12 16:48 | +5 | BTC | DOWN | 0.64 | 0.71 | 0.38 |
| 10-12 16:48 | +10 stop | ZEC | DOWN | 0.69 | 0.80 | 0.85 |
| 10-12 16:48 | +20 | ZEC | DOWN | 0.69 | 0.91 | 1.98 |
| 10-12 16:48 | +15 | ZEC | DOWN | 0.69 | 0.86 | 1.48 |
| 10-12 16:48 | +10 | ZEC | DOWN | 0.69 | 0.80 | 0.85 |
| 10-12 16:48 | +5 | ZEC | DOWN | 0.69 | 0.78 | 0.63 |
| 10-12 16:48 | +10 stop | HYPE | UP | 0.66 | 0.49 | -2.04 |
| 10-12 16:48 | +20 | HYPE | UP | 0.66 | open |  |
| 10-12 16:48 | +15 | HYPE | UP | 0.66 | open |  |
| 10-12 16:48 | +10 | HYPE | UP | 0.66 | open |  |
| 10-12 16:48 | +5 | HYPE | UP | 0.66 | open |  |
| 10-12 16:48 | +10 stop | DOGE | UP | 0.57 | 0.42 | -1.86 |
| 10-12 16:46 | +10 stop | BTC | DOWN | 0.69 | 0.84 | 1.25 |
| 10-12 16:46 | +20 | BTC | DOWN | 0.69 | 0.91 | 1.93 |
| 10-12 16:46 | +15 | BTC | DOWN | 0.69 | 0.84 | 1.25 |
| 10-12 16:46 | +10 | BTC | DOWN | 0.69 | 0.84 | 1.25 |
| 10-12 16:46 | +5 | BTC | DOWN | 0.69 | 0.74 | 0.21 |
| 10-12 16:46 | +10 stop | SOL | DOWN | 0.59 | 0.43 | -1.95 |
| 10-12 16:46 | +20 | SOL | DOWN | 0.59 | 0.79 | 1.71 |
| 10-12 16:46 | +15 | SOL | DOWN | 0.60 | 0.76 | 1.30 |
| 10-12 16:46 | +10 | SOL | DOWN | 0.60 | 0.76 | 1.30 |
| 10-12 16:46 | +5 | SOL | DOWN | 0.60 | 0.68 | 0.47 |
| 10-12 16:46 | +10 stop | DOGE | DOWN | 0.63 | 0.45 | -2.15 |
| 10-12 16:46 | +20 | DOGE | DOWN | 0.63 | 0.85 | 1.94 |
| 10-12 16:46 | +15 | DOGE | DOWN | 0.63 | 0.79 | 1.31 |
| 10-12 16:46 | +10 | DOGE | DOWN | 0.63 | 0.75 | 0.89 |
| 10-12 16:46 | +5 | DOGE | DOWN | 0.63 | 0.75 | 0.89 |
| 10-12 16:46 | +10 stop | BNB | DOWN | 0.63 | 0.76 | 1.00 |
| 10-12 16:46 | +20 | BNB | DOWN | 0.63 | 0.84 | 1.83 |
| 10-12 16:46 | +15 | BNB | DOWN | 0.63 | 0.84 | 1.83 |
| 10-12 16:46 | +10 | BNB | DOWN | 0.63 | 0.76 | 1.00 |
| 10-12 16:46 | +5 | BNB | DOWN | 0.63 | 0.76 | 1.00 |
| 10-12 16:41 | +10 stop | ETH | UP | 0.67 | 0.30 | -4.01 |
| 10-12 16:41 | +20 | ETH | UP | 0.68 | no | -6.96 |
| 10-12 16:41 | +15 | ETH | UP | 0.68 | no | -6.96 |
| 10-12 16:41 | +10 | ETH | UP | 0.69 | no | -7.05 |
| 10-12 16:41 | +10 stop | BTC | UP | 0.66 | 0.28 | -4.11 |
| 10-12 16:41 | +20 | BTC | UP | 0.64 | no | -6.57 |
| 10-12 16:41 | +15 | BTC | UP | 0.62 | no | -6.37 |
