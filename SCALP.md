# Range-Scalp Bot

*Updated Wed Oct 14 13:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 16011 | 13872 | 2139 (27) | 3 | $-5044.84 | -5.0% |
| **+10¢** | 12116 | 9635 | 2481 (39) | 4 | $-4656.35 | -6.1% |
| **+15¢** | 10185 | 7520 | 2665 (58) | 4 | $-4178.05 | -6.5% |
| **+20¢** | 9056 | 6260 | 2796 (75) | 4 | $-3712.71 | -6.5% |
| **+10¢ (15¢ stop)** | 19715 | 19665 | 50 (29) | 0 | $-7586.68 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 13:12 | +10 stop | XRP | UP | 0.52 | 0.34 | -2.14 |
| 10-14 13:12 | +5 | XRP | UP | 0.52 | 0.60 | 0.45 |
| 10-14 13:11 | +10 stop | BTC | UP | 0.54 | 0.13 | -4.36 |
| 10-14 13:11 | +10 stop | DOGE | UP | 0.53 | 0.69 | 1.27 |
| 10-14 13:10 | +10 stop | HYPE | UP | 0.46 | 0.72 | 2.27 |
| 10-14 13:10 | +10 stop | BTC | UP | 0.53 | 0.65 | 0.86 |
| 10-14 13:10 | +10 stop | DOGE | UP | 0.62 | 0.46 | -1.95 |
| 10-14 13:09 | +10 stop | SOL | UP | 0.67 | 0.80 | 1.02 |
| 10-14 13:09 | +10 | SOL | UP | 0.66 | 0.76 | 0.71 |
| 10-14 13:09 | +5 | SOL | UP | 0.66 | 0.75 | 0.60 |
| 10-14 13:09 | +10 stop | XRP | UP | 0.64 | 0.74 | 0.69 |
| 10-14 13:09 | +10 stop | ZEC | DOWN | 0.60 | 0.77 | 1.40 |
| 10-14 13:09 | +10 stop | HYPE | DOWN | 0.62 | 0.46 | -1.95 |
| 10-14 13:08 | +10 stop | BNB | UP | 0.48 | 0.65 | 1.36 |
| 10-14 13:08 | +10 stop | SOL | UP | 0.51 | 0.65 | 1.06 |
| 10-14 13:08 | +10 | SOL | UP | 0.51 | 0.65 | 1.06 |
| 10-14 13:08 | +5 | SOL | UP | 0.51 | 0.65 | 1.06 |
| 10-14 13:08 | +10 stop | DOGE | UP | 0.39 | 0.56 | 1.35 |
| 10-14 13:08 | +10 stop | BTC | UP | 0.42 | 0.58 | 1.24 |
| 10-14 13:08 | +10 stop | ZEC | DOWN | 0.54 | 0.68 | 1.06 |
| 10-14 13:07 | +10 stop | BTC | DOWN | 0.56 | 0.41 | -1.85 |
| 10-14 13:07 | +10 stop | DOGE | DOWN | 0.58 | 0.40 | -2.15 |
| 10-14 13:07 | +15 | DOGE | DOWN | 0.58 | 0.78 | 1.69 |
| 10-14 13:07 | +10 | DOGE | DOWN | 0.58 | 0.78 | 1.69 |
| 10-14 13:07 | +10 stop | HYPE | DOWN | 0.62 | 0.47 | -1.85 |
| 10-14 13:07 | +10 | HYPE | DOWN | 0.62 | 0.88 | 2.35 |
| 10-14 13:06 | +10 stop | SOL | UP | 0.51 | 0.68 | 1.36 |
| 10-14 13:05 | +10 stop | XRP | UP | 0.57 | 0.73 | 1.28 |
| 10-14 13:05 | +10 stop | ETH | UP | 0.60 | 0.76 | 1.30 |
| 10-14 13:05 | +10 stop | ZEC | DOWN | 0.61 | 0.73 | 0.89 |
| 10-14 13:05 | +10 stop | DOGE | DOWN | 0.45 | 0.57 | 0.84 |
| 10-14 13:05 | +15 | DOGE | DOWN | 0.46 | 0.61 | 1.15 |
| 10-14 13:05 | +10 | DOGE | DOWN | 0.46 | 0.57 | 0.74 |
| 10-14 13:05 | +10 stop | HYPE | DOWN | 0.54 | 0.64 | 0.65 |
| 10-14 13:05 | +10 | HYPE | DOWN | 0.54 | 0.64 | 0.65 |
| 10-14 13:05 | +10 stop | BNB | DOWN | 0.51 | 0.31 | -2.32 |
| 10-14 13:04 | +5 | DOGE | DOWN | 0.62 | 0.78 | 1.30 |
| 10-14 13:04 | +5 | HYPE | UP | 0.54 | 0.72 | 1.43 |
| 10-14 13:04 | +20 | SOL | UP | 0.59 | 0.80 | 1.81 |
| 10-14 13:04 | +5 | SOL | UP | 0.59 | 0.68 | 0.57 |
