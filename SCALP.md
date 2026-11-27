# Range-Scalp Bot

*Updated Fri Nov 27 14:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 73601 | 64227 | 9374 (171) | 1 | $-19596.82 | -4.2% |
| **+10¢** | 54847 | 43901 | 10946 (216) | 1 | $-18227.49 | -5.3% |
| **+15¢** | 45931 | 34142 | 11789 (274) | 2 | $-16320.08 | -5.7% |
| **+20¢** | 40879 | 28465 | 12414 (340) | 2 | $-14724.37 | -5.7% |
| **+10¢ (15¢ stop)** | 89631 | 89412 | 219 (135) | 0 | $-33130.13 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-27 14:51 | +10 stop | ZEC | DOWN | 0.62 | 0.76 | 1.10 |
| 11-27 14:51 | +10 | ZEC | DOWN | 0.62 | 0.76 | 1.10 |
| 11-27 14:51 | +5 | ZEC | DOWN | 0.66 | 0.76 | 0.71 |
| 11-27 14:47 | +10 stop | HYPE | DOWN | 0.68 | 0.83 | 1.24 |
| 11-27 14:46 | +10 stop | SOL | DOWN | 0.70 | 0.84 | 1.15 |
| 11-27 14:46 | +20 | SOL | DOWN | 0.70 | 0.90 | 1.78 |
| 11-27 14:46 | +15 | SOL | DOWN | 0.70 | 0.87 | 1.47 |
| 11-27 14:46 | +10 | SOL | DOWN | 0.70 | 0.84 | 1.15 |
| 11-27 14:46 | +5 | SOL | DOWN | 0.69 | 0.78 | 0.62 |
| 11-27 14:46 | +10 stop | BNB | DOWN | 0.71 | 0.81 | 0.74 |
| 11-27 14:46 | +20 | BNB | DOWN | 0.71 | 0.93 | 1.99 |
| 11-27 14:46 | +15 | BNB | DOWN | 0.71 | 0.89 | 1.58 |
| 11-27 14:46 | +10 | BNB | DOWN | 0.71 | 0.81 | 0.74 |
| 11-27 14:46 | +5 | BNB | DOWN | 0.71 | 0.79 | 0.53 |
| 11-27 14:46 | +10 stop | XRP | DOWN | 0.70 | 0.81 | 0.84 |
| 11-27 14:46 | +20 | XRP | DOWN | 0.70 | 0.95 | 2.33 |
| 11-27 14:46 | +15 | XRP | DOWN | 0.70 | 0.86 | 1.36 |
| 11-27 14:46 | +10 | XRP | DOWN | 0.70 | 0.81 | 0.84 |
| 11-27 14:46 | +5 | XRP | DOWN | 0.70 | 0.77 | 0.42 |
| 11-27 14:46 | +10 stop | ETH | DOWN | 0.70 | 0.82 | 0.94 |
| 11-27 14:46 | +20 | ETH | DOWN | 0.70 | 0.93 | 2.13 |
| 11-27 14:46 | +15 | ETH | DOWN | 0.70 | 0.88 | 1.57 |
| 11-27 14:46 | +10 | ETH | DOWN | 0.70 | 0.82 | 0.94 |
| 11-27 14:46 | +5 | ETH | DOWN | 0.70 | 0.78 | 0.52 |
| 11-27 14:45 | +10 stop | ZEC | UP | 0.49 | 0.61 | 0.85 |
| 11-27 14:45 | +20 | ZEC | UP | 0.49 | open |  |
| 11-27 14:45 | +15 | ZEC | UP | 0.49 | open |  |
| 11-27 14:45 | +10 | ZEC | UP | 0.49 | 0.61 | 0.85 |
| 11-27 14:45 | +5 | ZEC | UP | 0.51 | 0.61 | 0.65 |
| 11-27 14:45 | +10 stop | HYPE | UP | 0.59 | 0.37 | -2.52 |
| 11-27 14:45 | +20 | HYPE | UP | 0.59 | open |  |
| 11-27 14:45 | +15 | HYPE | UP | 0.58 | open |  |
| 11-27 14:45 | +10 | HYPE | UP | 0.59 | open |  |
| 11-27 14:45 | +5 | HYPE | UP | 0.60 | open |  |
| 11-27 08:49 | +5 | SOL | UP | 0.65 | yes | 3.34 |
| 11-27 08:48 | +10 stop | SOL | UP | 0.61 | yes | 3.72 |
| 11-27 08:48 | +10 | SOL | UP | 0.61 | yes | 3.73 |
| 11-27 08:48 | +5 | SOL | UP | 0.61 | 0.69 | 0.48 |
| 11-27 08:48 | +10 stop | ZEC | UP | 0.68 | yes | 3.04 |
| 11-27 08:48 | +20 | ZEC | UP | 0.69 | yes | 2.95 |
