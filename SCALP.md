# Range-Scalp Bot

*Updated Tue Oct 13 19:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 14826 | 12829 | 1997 (27) | 1 | $-4758.34 | -5.1% |
| **+10¢** | 11219 | 8900 | 2319 (39) | 1 | $-4446.82 | -6.3% |
| **+15¢** | 9434 | 6952 | 2482 (57) | 1 | $-3948.54 | -6.7% |
| **+20¢** | 8395 | 5807 | 2588 (73) | 1 | $-3402.82 | -6.5% |
| **+10¢ (15¢ stop)** | 18193 | 18143 | 50 (29) | 1 | $-7053.26 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-13 19:08 | +10 stop | NEAR | UP | 0.62 | open |  |
| 10-13 19:06 | +10 stop | ETH | UP | 0.66 | 0.82 | 1.33 |
| 10-13 19:06 | +20 | ETH | UP | 0.65 | 0.91 | 2.37 |
| 10-13 19:06 | +15 | ETH | UP | 0.65 | 0.82 | 1.43 |
| 10-13 19:06 | +10 | ETH | UP | 0.64 | 0.82 | 1.52 |
| 10-13 19:06 | +5 | ETH | UP | 0.69 | 0.82 | 1.04 |
| 10-13 19:06 | +10 stop | NEAR | UP | 0.49 | 0.60 | 0.75 |
| 10-13 19:02 | +10 stop | NEAR | UP | 0.71 | 0.82 | 0.84 |
| 10-13 19:02 | +10 stop | BNB | UP | 0.70 | 0.80 | 0.73 |
| 10-13 19:02 | +20 | BNB | UP | 0.70 | 0.91 | 1.90 |
| 10-13 19:02 | +15 | BNB | UP | 0.70 | 0.85 | 1.26 |
| 10-13 19:02 | +10 | BNB | UP | 0.70 | 0.80 | 0.73 |
| 10-13 19:02 | +5 | BNB | UP | 0.71 | 0.77 | 0.32 |
| 10-13 19:01 | +5 | ETH | UP | 0.71 | 0.80 | 0.63 |
| 10-13 19:01 | +10 stop | XRP | UP | 0.66 | 0.76 | 0.71 |
| 10-13 19:01 | +20 | XRP | UP | 0.66 | 0.86 | 1.75 |
| 10-13 19:01 | +15 | XRP | UP | 0.66 | 0.83 | 1.44 |
| 10-13 19:01 | +10 | XRP | UP | 0.66 | 0.76 | 0.71 |
| 10-13 19:01 | +5 | XRP | UP | 0.66 | 0.76 | 0.71 |
| 10-13 19:01 | +10 stop | ETH | UP | 0.59 | 0.70 | 0.73 |
| 10-13 19:01 | +20 | ETH | UP | 0.59 | 0.80 | 1.81 |
| 10-13 19:01 | +15 | ETH | UP | 0.59 | 0.75 | 1.29 |
| 10-13 19:01 | +10 | ETH | UP | 0.60 | 0.70 | 0.68 |
| 10-13 19:01 | +5 | ETH | UP | 0.60 | 0.65 | 0.17 |
| 10-13 19:01 | +10 stop | SOL | UP | 0.62 | 0.75 | 0.99 |
| 10-13 19:01 | +20 | SOL | UP | 0.62 | 0.82 | 1.72 |
| 10-13 19:01 | +15 | SOL | UP | 0.62 | 0.79 | 1.41 |
| 10-13 19:01 | +10 | SOL | UP | 0.62 | 0.75 | 0.99 |
| 10-13 19:01 | +5 | SOL | UP | 0.62 | 0.67 | 0.17 |
| 10-13 19:00 | +10 stop | NEAR | DOWN | 0.56 | 0.38 | -2.15 |
| 10-13 19:00 | +20 | NEAR | DOWN | 0.56 | open |  |
| 10-13 19:00 | +15 | NEAR | DOWN | 0.56 | open |  |
| 10-13 19:00 | +10 | NEAR | DOWN | 0.56 | open |  |
| 10-13 19:00 | +5 | NEAR | DOWN | 0.56 | open |  |
| 10-13 19:00 | +10 stop | HYPE | UP | 0.65 | 0.75 | 0.70 |
| 10-13 19:00 | +20 | HYPE | UP | 0.65 | 0.85 | 1.75 |
| 10-13 19:00 | +15 | HYPE | UP | 0.65 | 0.84 | 1.64 |
| 10-13 19:00 | +10 | HYPE | UP | 0.65 | 0.75 | 0.70 |
| 10-13 19:00 | +5 | HYPE | UP | 0.65 | 0.72 | 0.39 |
| 10-13 19:00 | +10 stop | BTC | UP | 0.65 | 0.77 | 0.91 |
