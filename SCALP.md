# Range-Scalp Bot

*Updated Tue Oct 20 02:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 24986 | 21754 | 3232 (31) | 0 | $-7305.86 | -4.6% |
| **+10¢** | 18794 | 15061 | 3733 (46) | 0 | $-6480.73 | -5.5% |
| **+15¢** | 15729 | 11708 | 4021 (70) | 0 | $-5843.95 | -5.9% |
| **+20¢** | 13908 | 9698 | 4210 (88) | 0 | $-5245.79 | -6.0% |
| **+10¢ (15¢ stop)** | 30656 | 30604 | 52 (30) | 0 | $-11413.61 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 02:46 | +10 stop | ETH | UP | 0.69 | 0.86 | 1.46 |
| 10-20 02:46 | +20 | ETH | UP | 0.69 | 0.90 | 1.91 |
| 10-20 02:46 | +15 | ETH | UP | 0.69 | 0.86 | 1.46 |
| 10-20 02:46 | +10 | ETH | UP | 0.69 | 0.86 | 1.46 |
| 10-20 02:46 | +5 | ETH | UP | 0.69 | 0.78 | 0.62 |
| 10-20 02:46 | +10 stop | SOL | UP | 0.71 | 0.84 | 1.05 |
| 10-20 02:46 | +20 | SOL | UP | 0.71 | 0.92 | 1.86 |
| 10-20 02:46 | +15 | SOL | UP | 0.71 | 0.88 | 1.47 |
| 10-20 02:46 | +10 | SOL | UP | 0.71 | 0.84 | 1.05 |
| 10-20 02:46 | +5 | SOL | UP | 0.71 | 0.78 | 0.42 |
| 10-20 02:46 | +10 stop | BNB | UP | 0.66 | 0.83 | 1.44 |
| 10-20 02:46 | +20 | BNB | UP | 0.66 | 0.86 | 1.75 |
| 10-20 02:46 | +15 | BNB | UP | 0.66 | 0.83 | 1.41 |
| 10-20 02:46 | +10 | BNB | UP | 0.66 | 0.83 | 1.41 |
| 10-20 02:46 | +5 | BNB | UP | 0.66 | 0.74 | 0.47 |
| 10-20 02:42 | +10 stop | ETH | DOWN | 0.62 | 0.86 | 2.14 |
| 10-20 02:42 | +10 stop | NEAR | DOWN | 0.49 | 0.64 | 1.15 |
| 10-20 02:42 | +10 stop | BTC | DOWN | 0.71 | 0.93 | 1.99 |
| 10-20 02:42 | +10 stop | HYPE | DOWN | 0.53 | 0.64 | 0.75 |
| 10-20 02:42 | +15 | HYPE | DOWN | 0.53 | 0.82 | 2.61 |
| 10-20 02:41 | +10 stop | ZEC | DOWN | 0.62 | 0.74 | 0.89 |
| 10-20 02:41 | +10 stop | XRP | DOWN | 0.64 | 0.46 | -2.15 |
| 10-20 02:41 | +10 stop | SOL | UP | 0.71 | 0.81 | 0.76 |
| 10-20 02:41 | +10 stop | ETH | DOWN | 0.54 | 0.77 | 1.99 |
| 10-20 02:41 | +10 stop | XRP | DOWN | 0.47 | 0.57 | 0.64 |
| 10-20 02:41 | +10 stop | NEAR | DOWN | 0.48 | 0.62 | 1.05 |
| 10-20 02:41 | +10 stop | BTC | DOWN | 0.58 | 0.77 | 1.59 |
| 10-20 02:39 | +10 stop | HYPE | DOWN | 0.59 | 0.71 | 0.88 |
| 10-20 02:39 | +20 | HYPE | DOWN | 0.55 | 0.82 | 2.37 |
| 10-20 02:39 | +15 | HYPE | DOWN | 0.55 | 0.71 | 1.23 |
| 10-20 02:39 | +10 stop | ZEC | DOWN | 0.65 | 0.45 | -2.34 |
| 10-20 02:39 | +10 stop | SOL | DOWN | 0.64 | 0.47 | -2.05 |
| 10-20 02:37 | +10 stop | HYPE | DOWN | 0.66 | 0.87 | 1.86 |
| 10-20 02:36 | +10 stop | BNB | DOWN | 0.71 | 0.90 | 1.69 |
| 10-20 02:36 | +10 stop | BTC | DOWN | 0.67 | 0.83 | 1.34 |
| 10-20 02:36 | +10 stop | XRP | UP | 0.54 | 0.35 | -2.24 |
| 10-20 02:36 | +10 | XRP | UP | 0.54 | no | -5.58 |
| 10-20 02:36 | +5 | XRP | UP | 0.54 | no | -5.58 |
| 10-20 02:35 | +10 stop | DOGE | DOWN | 0.59 | 0.77 | 1.50 |
| 10-20 02:35 | +20 | SOL | UP | 0.69 | 0.90 | 1.89 |
