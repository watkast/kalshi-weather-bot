# Range-Scalp Bot

*Updated Wed Nov 04 20:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47479 | 41341 | 6138 (73) | 3 | $-13697.88 | -4.6% |
| **+10¢** | 35469 | 28349 | 7120 (98) | 5 | $-12526.85 | -5.6% |
| **+15¢** | 29702 | 22036 | 7666 (126) | 8 | $-11486.91 | -6.2% |
| **+20¢** | 26390 | 18361 | 8029 (166) | 8 | $-10144.11 | -6.1% |
| **+10¢ (15¢ stop)** | 57878 | 57785 | 93 (56) | 1 | $-21583.62 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 20:11 | +10 stop | NEAR | UP | 0.65 | open |  |
| 11-04 20:11 | +15 | NEAR | UP | 0.65 | open |  |
| 11-04 20:11 | +10 | NEAR | UP | 0.65 | open |  |
| 11-04 20:11 | +5 | NEAR | UP | 0.65 | 0.74 | 0.63 |
| 11-04 20:07 | +10 stop | NEAR | UP | 0.63 | 0.80 | 1.41 |
| 11-04 20:07 | +15 | NEAR | UP | 0.63 | 0.80 | 1.41 |
| 11-04 20:07 | +10 | NEAR | UP | 0.63 | 0.80 | 1.41 |
| 11-04 20:07 | +5 | NEAR | UP | 0.63 | 0.80 | 1.41 |
| 11-04 20:07 | +10 stop | XRP | UP | 0.69 | 0.54 | -1.83 |
| 11-04 20:07 | +10 stop | SOL | UP | 0.69 | 0.53 | -1.93 |
| 11-04 20:06 | +10 stop | DOGE | DOWN | 0.31 | 0.60 | 2.58 |
| 11-04 20:06 | +10 stop | ETH | DOWN | 0.29 | 0.57 | 2.47 |
| 11-04 20:06 | +10 stop | SOL | DOWN | 0.63 | 0.43 | -2.35 |
| 11-04 20:06 | +10 stop | HYPE | DOWN | 0.68 | 0.78 | 0.71 |
| 11-04 20:06 | +10 | HYPE | DOWN | 0.68 | 0.78 | 0.71 |
| 11-04 20:06 | +5 | HYPE | DOWN | 0.68 | 0.75 | 0.40 |
| 11-04 20:06 | +10 stop | BNB | UP | 0.65 | 0.75 | 0.70 |
| 11-04 20:05 | +10 stop | DOGE | UP | 0.57 | 0.40 | -2.05 |
| 11-04 20:05 | +10 stop | ETH | UP | 0.55 | 0.39 | -1.95 |
| 11-04 20:05 | +10 stop | BTC | DOWN | 0.63 | 0.75 | 0.89 |
| 11-04 20:05 | +10 | BTC | DOWN | 0.63 | 0.75 | 0.89 |
| 11-04 20:05 | +5 | BTC | DOWN | 0.63 | 0.75 | 0.89 |
| 11-04 20:05 | +10 | XRP | DOWN | 0.62 | open |  |
| 11-04 20:05 | +5 | XRP | DOWN | 0.62 | open |  |
| 11-04 20:04 | +10 stop | ZEC | DOWN | 0.53 | 0.32 | -2.44 |
| 11-04 20:04 | +15 | ZEC | DOWN | 0.53 | open |  |
| 11-04 20:04 | +5 | NEAR | DOWN | 0.64 | 0.78 | 1.10 |
| 11-04 20:04 | +10 stop | DOGE | DOWN | 0.61 | 0.44 | -2.05 |
| 11-04 20:04 | +10 stop | NEAR | DOWN | 0.67 | 0.78 | 0.81 |
| 11-04 20:03 | +10 stop | XRP | DOWN | 0.69 | 0.41 | -3.08 |
| 11-04 20:03 | +10 stop | SOL | DOWN | 0.69 | 0.53 | -1.93 |
| 11-04 20:03 | +5 | ETH | UP | 0.65 | 0.75 | 0.70 |
| 11-04 20:03 | +10 stop | NEAR | UP | 0.60 | 0.45 | -1.85 |
| 11-04 20:03 | +10 stop | DOGE | UP | 0.59 | 0.36 | -2.64 |
| 11-04 20:02 | +10 stop | BNB | UP | 0.71 | 0.49 | -2.53 |
| 11-04 20:02 | +5 | BNB | UP | 0.71 | 0.82 | 0.84 |
| 11-04 20:02 | +10 stop | ZEC | UP | 0.63 | 0.42 | -2.45 |
| 11-04 20:02 | +10 | ZEC | UP | 0.62 | 0.72 | 0.68 |
| 11-04 20:02 | +5 | ZEC | UP | 0.62 | 0.67 | 0.17 |
| 11-04 20:02 | +10 stop | ETH | UP | 0.61 | 0.46 | -1.85 |
