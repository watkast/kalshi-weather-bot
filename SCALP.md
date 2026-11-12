# Range-Scalp Bot

*Updated Thu Nov 12 12:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56882 | 49584 | 7298 (101) | 0 | $-15665.41 | -4.4% |
| **+10¢** | 42512 | 33999 | 8513 (133) | 0 | $-14590.16 | -5.5% |
| **+15¢** | 35645 | 26481 | 9164 (167) | 0 | $-13204.93 | -5.9% |
| **+20¢** | 31754 | 22139 | 9615 (217) | 0 | $-11587.38 | -5.8% |
| **+10¢ (15¢ stop)** | 69347 | 69219 | 128 (78) | 0 | $-25627.61 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 12:21 | +5 | BTC | DOWN | 0.68 | 0.88 | 1.76 |
| 11-12 12:20 | +5 | BTC | DOWN | 0.55 | 0.61 | 0.25 |
| 11-12 12:19 | +10 stop | ZEC | DOWN | 0.56 | 0.68 | 0.86 |
| 11-12 12:19 | +10 stop | BTC | DOWN | 0.55 | 0.68 | 0.96 |
| 11-12 12:19 | +20 | BTC | DOWN | 0.55 | 0.88 | 3.04 |
| 11-12 12:19 | +15 | BTC | DOWN | 0.55 | 0.88 | 3.04 |
| 11-12 12:19 | +10 | BTC | DOWN | 0.55 | 0.68 | 0.96 |
| 11-12 12:19 | +5 | BTC | DOWN | 0.55 | 0.60 | 0.15 |
| 11-12 12:19 | +10 stop | SOL | DOWN | 0.63 | 0.86 | 2.04 |
| 11-12 12:19 | +20 | SOL | DOWN | 0.63 | 0.86 | 2.04 |
| 11-12 12:19 | +15 | SOL | DOWN | 0.63 | 0.86 | 2.04 |
| 11-12 12:19 | +10 | SOL | DOWN | 0.63 | 0.86 | 2.04 |
| 11-12 12:19 | +5 | SOL | DOWN | 0.64 | 0.72 | 0.48 |
| 11-12 12:19 | +10 stop | ETH | DOWN | 0.65 | 0.78 | 1.01 |
| 11-12 12:19 | +20 | ETH | DOWN | 0.65 | 0.88 | 2.06 |
| 11-12 12:19 | +15 | ETH | DOWN | 0.65 | 0.88 | 2.06 |
| 11-12 12:19 | +10 | ETH | DOWN | 0.65 | 0.78 | 1.01 |
| 11-12 12:19 | +5 | ETH | DOWN | 0.66 | 0.71 | 0.19 |
| 11-12 12:19 | +10 stop | XRP | DOWN | 0.65 | 0.75 | 0.70 |
| 11-12 12:19 | +5 | XRP | DOWN | 0.66 | 0.75 | 0.60 |
| 11-12 12:19 | +5 | DOGE | DOWN | 0.68 | 0.77 | 0.61 |
| 11-12 12:18 | +5 | XRP | DOWN | 0.51 | 0.60 | 0.55 |
| 11-12 12:18 | +10 stop | NEAR | DOWN | 0.60 | 0.70 | 0.68 |
| 11-12 12:18 | +10 | NEAR | DOWN | 0.60 | 0.70 | 0.68 |
| 11-12 12:18 | +5 | NEAR | DOWN | 0.60 | 0.70 | 0.68 |
| 11-12 12:18 | +10 stop | DOGE | DOWN | 0.56 | 0.66 | 0.66 |
| 11-12 12:18 | +10 | DOGE | DOWN | 0.56 | 0.66 | 0.66 |
| 11-12 12:18 | +5 | DOGE | DOWN | 0.56 | 0.61 | 0.15 |
| 11-12 12:18 | +5 | ZEC | DOWN | 0.61 | 0.68 | 0.37 |
| 11-12 12:15 | +10 stop | BNB | DOWN | 0.70 | 0.80 | 0.73 |
| 11-12 12:15 | +20 | BNB | DOWN | 0.70 | 0.97 | 2.54 |
| 11-12 12:15 | +15 | BNB | DOWN | 0.70 | 0.86 | 1.36 |
| 11-12 12:15 | +10 | BNB | DOWN | 0.70 | 0.80 | 0.73 |
| 11-12 12:15 | +5 | BNB | DOWN | 0.70 | 0.76 | 0.32 |
| 11-12 12:15 | +10 stop | XRP | DOWN | 0.65 | 0.49 | -1.94 |
| 11-12 12:15 | +20 | XRP | DOWN | 0.65 | 0.86 | 1.85 |
| 11-12 12:15 | +15 | XRP | DOWN | 0.65 | 0.86 | 1.85 |
| 11-12 12:15 | +10 | XRP | DOWN | 0.65 | 0.75 | 0.70 |
| 11-12 12:15 | +5 | XRP | DOWN | 0.64 | 0.69 | 0.18 |
| 11-12 12:15 | +10 stop | NEAR | DOWN | 0.66 | 0.77 | 0.81 |
