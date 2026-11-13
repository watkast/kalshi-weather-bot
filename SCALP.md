# Range-Scalp Bot

*Updated Fri Nov 13 11:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58245 | 50824 | 7421 (102) | 4 | $-15717.43 | -4.3% |
| **+10¢** | 43520 | 34843 | 8677 (134) | 5 | $-14680.44 | -5.4% |
| **+15¢** | 36485 | 27142 | 9343 (169) | 5 | $-13236.29 | -5.8% |
| **+20¢** | 32505 | 22694 | 9811 (220) | 5 | $-11621.93 | -5.7% |
| **+10¢ (15¢ stop)** | 70967 | 70838 | 129 (79) | 4 | $-26096.37 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 11:56 | +10 stop | BTC | DOWN | 0.61 | open |  |
| 11-13 11:56 | +10 stop | DOGE | UP | 0.60 | open |  |
| 11-13 11:55 | +10 stop | HYPE | DOWN | 0.47 | open |  |
| 11-13 11:55 | +15 | HYPE | DOWN | 0.47 | open |  |
| 11-13 11:55 | +10 | HYPE | DOWN | 0.48 | open |  |
| 11-13 11:55 | +5 | HYPE | DOWN | 0.48 | 0.55 | 0.34 |
| 11-13 11:55 | +10 stop | XRP | UP | 0.62 | open |  |
| 11-13 11:55 | +10 | XRP | UP | 0.62 | open |  |
| 11-13 11:55 | +5 | XRP | UP | 0.62 | open |  |
| 11-13 11:54 | +15 | ZEC | DOWN | 0.70 | 0.85 | 1.26 |
| 11-13 11:54 | +10 stop | ZEC | DOWN | 0.71 | 0.85 | 1.16 |
| 11-13 11:54 | +10 | ZEC | DOWN | 0.70 | 0.85 | 1.26 |
| 11-13 11:54 | +5 | ZEC | DOWN | 0.70 | 0.78 | 0.52 |
| 11-13 11:54 | +10 stop | HYPE | DOWN | 0.53 | 0.65 | 0.86 |
| 11-13 11:54 | +20 | HYPE | DOWN | 0.53 | open |  |
| 11-13 11:54 | +15 | HYPE | DOWN | 0.53 | 0.72 | 1.57 |
| 11-13 11:54 | +10 | HYPE | DOWN | 0.53 | 0.65 | 0.86 |
| 11-13 11:54 | +5 | HYPE | DOWN | 0.53 | 0.58 | 0.14 |
| 11-13 11:54 | +10 stop | SOL | UP | 0.63 | 0.40 | -2.64 |
| 11-13 11:54 | +10 | SOL | UP | 0.63 | open |  |
| 11-13 11:54 | +5 | SOL | UP | 0.63 | open |  |
| 11-13 11:54 | +10 stop | DOGE | UP | 0.71 | 0.55 | -1.93 |
| 11-13 11:54 | +10 stop | ETH | DOWN | 0.47 | 0.60 | 0.95 |
| 11-13 11:54 | +15 | ETH | DOWN | 0.47 | 0.66 | 1.56 |
| 11-13 11:54 | +10 | ETH | DOWN | 0.47 | 0.60 | 0.95 |
| 11-13 11:54 | +5 | ETH | DOWN | 0.47 | 0.60 | 0.95 |
| 11-13 11:54 | +10 stop | SOL | DOWN | 0.56 | 0.67 | 0.76 |
| 11-13 11:54 | +10 | SOL | DOWN | 0.57 | 0.67 | 0.66 |
| 11-13 11:54 | +5 | SOL | DOWN | 0.59 | 0.67 | 0.47 |
| 11-13 11:53 | +10 | DOGE | DOWN | 0.68 | open |  |
| 11-13 11:52 | +10 stop | BTC | DOWN | 0.54 | 0.32 | -2.54 |
| 11-13 11:52 | +10 stop | XRP | UP | 0.61 | 0.79 | 1.52 |
| 11-13 11:52 | +5 | DOGE | DOWN | 0.70 | open |  |
| 11-13 11:52 | +10 stop | SOL | DOWN | 0.59 | 0.72 | 0.98 |
| 11-13 11:52 | +20 | SOL | DOWN | 0.61 | open |  |
| 11-13 11:52 | +15 | SOL | DOWN | 0.61 | open |  |
| 11-13 11:52 | +10 | SOL | DOWN | 0.61 | 0.72 | 0.78 |
| 11-13 11:52 | +5 | SOL | DOWN | 0.61 | 0.72 | 0.78 |
| 11-13 11:51 | +5 | ETH | DOWN | 0.61 | 0.72 | 0.78 |
| 11-13 11:51 | +10 stop | BTC | UP | 0.68 | 0.45 | -2.64 |
