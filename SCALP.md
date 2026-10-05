# Range-Scalp Bot

*Updated Mon Oct 05 09:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3603 | 3091 | 512 (3) | 1 | $-1320.20 | -5.8% |
| **+10¢** | 2784 | 2196 | 588 (4) | 1 | $-1209.11 | -6.9% |
| **+15¢** | 2342 | 1722 | 620 (6) | 1 | $-1075.82 | -7.3% |
| **+20¢** | 2089 | 1443 | 646 (11) | 1 | $-940.27 | -7.2% |
| **+10¢ (15¢ stop)** | 4462 | 4461 | 1 (1) | 0 | $-1725.15 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 09:12 | +10 stop | DOGE | DOWN | 0.71 | 0.55 | -1.93 |
| 10-05 09:12 | +5 | DOGE | DOWN | 0.71 | 0.87 | 1.37 |
| 10-05 09:12 | +10 stop | HYPE | UP | 0.48 | 0.68 | 1.70 |
| 10-05 09:11 | +10 stop | HYPE | DOWN | 0.57 | 0.33 | -2.74 |
| 10-05 09:10 | +10 stop | SOL | DOWN | 0.65 | 0.82 | 1.43 |
| 10-05 09:10 | +10 | SOL | DOWN | 0.65 | 0.82 | 1.43 |
| 10-05 09:09 | +10 stop | HYPE | UP | 0.65 | 0.41 | -2.73 |
| 10-05 09:09 | +10 stop | XRP | UP | 0.61 | 0.31 | -3.32 |
| 10-05 09:09 | +10 stop | ETH | UP | 0.47 | 0.57 | 0.64 |
| 10-05 09:08 | +10 stop | NEAR | UP | 0.64 | 0.38 | -2.94 |
| 10-05 09:08 | +20 | NEAR | UP | 0.64 | open |  |
| 10-05 09:08 | +15 | NEAR | UP | 0.64 | open |  |
| 10-05 09:08 | +10 | NEAR | UP | 0.64 | open |  |
| 10-05 09:08 | +5 | NEAR | UP | 0.65 | open |  |
| 10-05 09:08 | +10 stop | SOL | DOWN | 0.52 | 0.66 | 1.06 |
| 10-05 09:08 | +10 | SOL | DOWN | 0.52 | 0.66 | 1.06 |
| 10-05 09:07 | +10 stop | XRP | UP | 0.61 | 0.72 | 0.78 |
| 10-05 09:07 | +5 | SOL | DOWN | 0.71 | 0.82 | 0.84 |
| 10-05 09:06 | +5 | BNB | UP | 0.69 | 0.78 | 0.63 |
| 10-05 09:06 | +10 stop | ZEC | UP | 0.70 | 0.84 | 1.15 |
| 10-05 09:06 | +20 | ZEC | UP | 0.70 | 0.90 | 1.78 |
| 10-05 09:06 | +15 | ZEC | UP | 0.70 | 0.86 | 1.36 |
| 10-05 09:06 | +10 | ZEC | UP | 0.70 | 0.84 | 1.15 |
| 10-05 09:06 | +5 | ZEC | UP | 0.70 | 0.78 | 0.52 |
| 10-05 09:05 | +10 stop | HYPE | UP | 0.65 | 0.49 | -1.94 |
| 10-05 09:05 | +10 stop | ETH | UP | 0.57 | 0.42 | -1.86 |
| 10-05 09:05 | +10 stop | NEAR | UP | 0.65 | 0.80 | 1.22 |
| 10-05 09:04 | +10 stop | HYPE | DOWN | 0.70 | 0.53 | -2.07 |
| 10-05 09:04 | +10 | HYPE | DOWN | 0.70 | 0.81 | 0.80 |
| 10-05 09:04 | +5 | HYPE | DOWN | 0.70 | 0.81 | 0.80 |
| 10-05 09:04 | +10 stop | DOGE | UP | 0.67 | 0.49 | -2.14 |
| 10-05 09:04 | +10 stop | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 10-05 09:04 | +20 | SOL | DOWN | 0.61 | 0.82 | 1.82 |
| 10-05 09:04 | +15 | SOL | DOWN | 0.61 | 0.82 | 1.82 |
| 10-05 09:04 | +10 | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 10-05 09:04 | +5 | SOL | DOWN | 0.61 | 0.69 | 0.48 |
| 10-05 09:04 | +5 | BNB | UP | 0.60 | 0.66 | 0.27 |
| 10-05 09:03 | +10 stop | NEAR | DOWN | 0.55 | 0.39 | -1.95 |
| 10-05 09:03 | +10 stop | ETH | UP | 0.57 | 0.41 | -1.95 |
| 10-05 09:03 | +10 stop | ZEC | UP | 0.56 | 0.71 | 1.17 |
