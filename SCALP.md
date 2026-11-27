# Range-Scalp Bot

*Updated Fri Nov 27 14:46 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 73596 | 64222 | 9374 (171) | 1 | $-19599.62 | -4.2% |
| **+10¢** | 54842 | 43896 | 10946 (216) | 1 | $-18232.26 | -5.3% |
| **+15¢** | 45927 | 34138 | 11789 (274) | 2 | $-16326.06 | -5.7% |
| **+20¢** | 40875 | 28461 | 12414 (340) | 2 | $-14732.60 | -5.7% |
| **+10¢ (15¢ stop)** | 89624 | 89405 | 219 (135) | 1 | $-33133.62 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-27 14:45 | +10 stop | ZEC | UP | 0.49 | 0.61 | 0.85 |
| 11-27 14:45 | +20 | ZEC | UP | 0.49 | open |  |
| 11-27 14:45 | +15 | ZEC | UP | 0.49 | open |  |
| 11-27 14:45 | +10 | ZEC | UP | 0.49 | 0.61 | 0.85 |
| 11-27 14:45 | +5 | ZEC | UP | 0.51 | 0.61 | 0.65 |
| 11-27 14:45 | +10 stop | HYPE | UP | 0.59 | open |  |
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
| 11-27 08:48 | +15 | ZEC | UP | 0.66 | yes | 3.24 |
| 11-27 08:48 | +10 | ZEC | UP | 0.66 | yes | 3.24 |
| 11-27 08:48 | +5 | ZEC | UP | 0.66 | yes | 3.24 |
| 11-27 08:48 | +10 stop | BTC | DOWN | 0.57 | no | 4.12 |
| 11-27 08:48 | +10 | BTC | DOWN | 0.57 | no | 4.12 |
| 11-27 08:47 | +5 | BNB | DOWN | 0.61 | no | 3.73 |
| 11-27 08:47 | +5 | HYPE | DOWN | 0.65 | no | 3.36 |
| 11-27 08:47 | +5 | XRP | DOWN | 0.63 | no | 3.53 |
| 11-27 08:47 | +10 stop | ETH | DOWN | 0.58 | yes | -5.98 |
| 11-27 08:47 | +20 | ETH | DOWN | 0.58 | yes | -5.98 |
| 11-27 08:47 | +15 | ETH | DOWN | 0.58 | yes | -5.98 |
| 11-27 08:47 | +10 | ETH | DOWN | 0.58 | yes | -5.98 |
| 11-27 08:47 | +5 | ETH | DOWN | 0.58 | yes | -5.98 |
| 11-27 08:47 | +5 | BTC | DOWN | 0.61 | no | 3.73 |
| 11-27 08:47 | +10 stop | SOL | UP | 0.56 | 0.68 | 0.86 |
| 11-27 08:47 | +20 | SOL | UP | 0.56 | yes | 4.22 |
| 11-27 08:47 | +15 | SOL | UP | 0.56 | yes | 4.22 |
| 11-27 08:47 | +10 | SOL | UP | 0.56 | 0.68 | 0.86 |
| 11-27 08:47 | +5 | SOL | UP | 0.56 | 0.68 | 0.86 |
| 11-27 08:47 | +10 stop | NEAR | DOWN | 0.61 | 0.45 | -1.95 |
| 11-27 08:47 | +20 | NEAR | DOWN | 0.61 | yes | -6.27 |
| 11-27 08:47 | +15 | NEAR | DOWN | 0.61 | yes | -6.27 |
| 11-27 08:47 | +10 | NEAR | DOWN | 0.62 | yes | -6.37 |
| 11-27 08:47 | +5 | NEAR | DOWN | 0.62 | yes | -6.37 |
