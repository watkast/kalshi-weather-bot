# Range-Scalp Bot

*Updated Wed Nov 11 12:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55792 | 48659 | 7133 (94) | 0 | $-15212.64 | -4.3% |
| **+10¢** | 41687 | 33369 | 8318 (124) | 0 | $-14133.35 | -5.4% |
| **+15¢** | 34953 | 25979 | 8974 (158) | 1 | $-12903.33 | -5.9% |
| **+20¢** | 31130 | 21717 | 9413 (208) | 2 | $-11265.77 | -5.8% |
| **+10¢ (15¢ stop)** | 67965 | 67844 | 121 (73) | 0 | $-24992.67 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 12:02 | +5 | SOL | DOWN | 0.68 | 0.75 | 0.40 |
| 11-11 12:02 | +5 | XRP | DOWN | 0.69 | 0.77 | 0.52 |
| 11-11 12:02 | +10 stop | BTC | DOWN | 0.64 | 0.77 | 1.00 |
| 11-11 12:02 | +20 | BTC | DOWN | 0.64 | 0.92 | 2.56 |
| 11-11 12:02 | +15 | BTC | DOWN | 0.64 | 0.92 | 2.56 |
| 11-11 12:02 | +10 | BTC | DOWN | 0.64 | 0.77 | 1.00 |
| 11-11 12:02 | +5 | BTC | DOWN | 0.64 | 0.77 | 1.00 |
| 11-11 12:01 | +10 stop | DOGE | DOWN | 0.66 | 0.48 | -2.14 |
| 11-11 12:01 | +20 | DOGE | DOWN | 0.68 | open |  |
| 11-11 12:01 | +15 | DOGE | DOWN | 0.68 | 0.86 | 1.55 |
| 11-11 12:01 | +10 | DOGE | DOWN | 0.68 | 0.86 | 1.55 |
| 11-11 12:01 | +5 | DOGE | DOWN | 0.68 | 0.75 | 0.40 |
| 11-11 12:01 | +10 stop | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 11-11 12:01 | +20 | ETH | DOWN | 0.65 | 0.88 | 2.06 |
| 11-11 12:01 | +15 | ETH | DOWN | 0.67 | 0.82 | 1.23 |
| 11-11 12:01 | +10 | ETH | DOWN | 0.67 | 0.78 | 0.81 |
| 11-11 12:01 | +5 | ETH | DOWN | 0.67 | 0.75 | 0.50 |
| 11-11 12:01 | +10 stop | XRP | DOWN | 0.61 | 0.77 | 1.30 |
| 11-11 12:01 | +20 | XRP | DOWN | 0.61 | 0.85 | 2.14 |
| 11-11 12:01 | +15 | XRP | DOWN | 0.61 | 0.77 | 1.30 |
| 11-11 12:01 | +10 | XRP | DOWN | 0.61 | 0.77 | 1.30 |
| 11-11 12:01 | +5 | XRP | DOWN | 0.60 | 0.65 | 0.17 |
| 11-11 12:01 | +10 stop | ZEC | DOWN | 0.58 | 0.79 | 1.80 |
| 11-11 12:01 | +20 | ZEC | DOWN | 0.58 | 0.79 | 1.80 |
| 11-11 12:01 | +15 | ZEC | DOWN | 0.58 | 0.79 | 1.80 |
| 11-11 12:01 | +10 | ZEC | DOWN | 0.58 | 0.79 | 1.80 |
| 11-11 12:01 | +5 | ZEC | DOWN | 0.58 | 0.64 | 0.25 |
| 11-11 12:01 | +10 stop | HYPE | DOWN | 0.65 | 0.79 | 1.12 |
| 11-11 12:01 | +20 | HYPE | DOWN | 0.65 | 0.88 | 2.06 |
| 11-11 12:01 | +15 | HYPE | DOWN | 0.66 | 0.88 | 1.96 |
| 11-11 12:01 | +10 | HYPE | DOWN | 0.66 | 0.79 | 1.02 |
| 11-11 12:01 | +5 | HYPE | DOWN | 0.66 | 0.74 | 0.50 |
| 11-11 12:01 | +10 stop | SOL | DOWN | 0.64 | 0.75 | 0.79 |
| 11-11 12:01 | +20 | SOL | DOWN | 0.64 | 0.90 | 2.36 |
| 11-11 12:01 | +15 | SOL | DOWN | 0.64 | 0.79 | 1.21 |
| 11-11 12:01 | +10 | SOL | DOWN | 0.63 | 0.75 | 0.89 |
| 11-11 12:01 | +5 | SOL | DOWN | 0.63 | 0.68 | 0.17 |
| 11-11 12:01 | +10 stop | NEAR | UP | 0.71 | 0.84 | 1.05 |
| 11-11 12:01 | +20 | NEAR | UP | 0.71 | open |  |
| 11-11 12:01 | +15 | NEAR | UP | 0.71 | open |  |
