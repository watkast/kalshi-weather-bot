# Range-Scalp Bot

*Updated Wed Nov 04 22:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47616 | 41458 | 6158 (73) | 2 | $-13752.20 | -4.6% |
| **+10¢** | 35580 | 28438 | 7142 (98) | 2 | $-12567.31 | -5.6% |
| **+15¢** | 29810 | 22118 | 7692 (126) | 2 | $-11514.46 | -6.2% |
| **+20¢** | 26488 | 18431 | 8057 (166) | 4 | $-10167.43 | -6.1% |
| **+10¢ (15¢ stop)** | 58045 | 57952 | 93 (56) | 1 | $-21594.77 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 22:24 | +10 stop | DOGE | UP | 0.60 | 0.76 | 1.30 |
| 11-04 22:24 | +20 | DOGE | UP | 0.60 | open |  |
| 11-04 22:24 | +15 | DOGE | UP | 0.60 | 0.76 | 1.30 |
| 11-04 22:24 | +10 | DOGE | UP | 0.60 | 0.76 | 1.30 |
| 11-04 22:24 | +5 | DOGE | UP | 0.60 | 0.76 | 1.30 |
| 11-04 22:24 | +10 stop | XRP | UP | 0.68 | 0.83 | 1.24 |
| 11-04 22:24 | +20 | XRP | UP | 0.68 | open |  |
| 11-04 22:24 | +15 | XRP | UP | 0.68 | 0.83 | 1.24 |
| 11-04 22:24 | +10 | XRP | UP | 0.68 | 0.83 | 1.24 |
| 11-04 22:24 | +5 | XRP | UP | 0.68 | 0.83 | 1.21 |
| 11-04 22:24 | +10 stop | SOL | UP | 0.60 | open |  |
| 11-04 22:24 | +20 | SOL | UP | 0.60 | open |  |
| 11-04 22:24 | +15 | SOL | UP | 0.60 | open |  |
| 11-04 22:24 | +10 | SOL | UP | 0.60 | open |  |
| 11-04 22:24 | +5 | SOL | UP | 0.60 | open |  |
| 11-04 22:24 | +10 stop | HYPE | DOWN | 0.71 | 0.84 | 1.05 |
| 11-04 22:23 | +10 stop | ZEC | DOWN | 0.61 | 0.76 | 1.20 |
| 11-04 22:22 | +10 stop | HYPE | UP | 0.56 | 0.34 | -2.54 |
| 11-04 22:20 | +5 | ZEC | UP | 0.64 | open |  |
| 11-04 22:19 | +10 stop | ZEC | UP | 0.57 | 0.38 | -2.25 |
| 11-04 22:19 | +20 | ZEC | UP | 0.57 | open |  |
| 11-04 22:19 | +15 | ZEC | UP | 0.57 | open |  |
| 11-04 22:19 | +10 | ZEC | UP | 0.57 | open |  |
| 11-04 22:19 | +5 | ZEC | UP | 0.57 | 0.63 | 0.25 |
| 11-04 22:18 | +10 stop | HYPE | UP | 0.59 | 0.71 | 0.88 |
| 11-04 22:17 | +10 stop | XRP | UP | 0.68 | 0.84 | 1.34 |
| 11-04 22:17 | +20 | XRP | UP | 0.68 | 0.91 | 2.08 |
| 11-04 22:17 | +15 | XRP | UP | 0.68 | 0.84 | 1.34 |
| 11-04 22:17 | +10 | XRP | UP | 0.68 | 0.84 | 1.34 |
| 11-04 22:17 | +5 | XRP | UP | 0.68 | 0.76 | 0.51 |
| 11-04 22:17 | +10 stop | SOL | UP | 0.60 | 0.75 | 1.19 |
| 11-04 22:17 | +20 | SOL | UP | 0.60 | 0.81 | 1.82 |
| 11-04 22:17 | +15 | SOL | UP | 0.62 | 0.78 | 1.30 |
| 11-04 22:17 | +10 | SOL | UP | 0.62 | 0.75 | 0.99 |
| 11-04 22:17 | +5 | SOL | UP | 0.62 | 0.75 | 0.99 |
| 11-04 22:17 | +10 stop | BTC | UP | 0.66 | 0.82 | 1.33 |
| 11-04 22:17 | +20 | BTC | UP | 0.66 | 0.88 | 1.96 |
| 11-04 22:17 | +15 | BTC | UP | 0.66 | 0.82 | 1.33 |
| 11-04 22:17 | +10 | BTC | UP | 0.66 | 0.82 | 1.33 |
| 11-04 22:17 | +5 | BTC | UP | 0.66 | 0.73 | 0.40 |
