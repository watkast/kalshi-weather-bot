# Range-Scalp Bot

*Updated Tue Nov 03 18:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46163 | 40195 | 5968 (72) | 0 | $-13295.56 | -4.6% |
| **+10¢** | 34458 | 27542 | 6916 (96) | 0 | $-12161.49 | -5.6% |
| **+15¢** | 28841 | 21407 | 7434 (124) | 1 | $-11084.07 | -6.1% |
| **+20¢** | 25621 | 17828 | 7793 (164) | 1 | $-9824.17 | -6.1% |
| **+10¢ (15¢ stop)** | 56319 | 56226 | 93 (56) | 0 | $-21124.98 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 18:24 | +10 stop | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-03 18:24 | +20 | BTC | DOWN | 0.64 | open |  |
| 11-03 18:24 | +15 | BTC | DOWN | 0.64 | open |  |
| 11-03 18:24 | +10 | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-03 18:24 | +5 | BTC | DOWN | 0.64 | 0.69 | 0.18 |
| 11-03 18:22 | +10 stop | HYPE | DOWN | 0.66 | 0.84 | 1.54 |
| 11-03 18:20 | +10 stop | SOL | DOWN | 0.66 | 0.78 | 0.91 |
| 11-03 18:20 | +20 | SOL | DOWN | 0.66 | 0.87 | 1.86 |
| 11-03 18:20 | +10 | SOL | DOWN | 0.65 | 0.78 | 1.01 |
| 11-03 18:20 | +5 | SOL | DOWN | 0.63 | 0.73 | 0.69 |
| 11-03 18:19 | +10 stop | SOL | DOWN | 0.69 | 0.79 | 0.73 |
| 11-03 18:19 | +15 | SOL | DOWN | 0.69 | 0.85 | 1.36 |
| 11-03 18:19 | +10 | SOL | DOWN | 0.69 | 0.79 | 0.73 |
| 11-03 18:19 | +5 | SOL | DOWN | 0.69 | 0.79 | 0.73 |
| 11-03 18:19 | +10 stop | ZEC | DOWN | 0.67 | 0.80 | 1.02 |
| 11-03 18:19 | +10 | ZEC | DOWN | 0.67 | 0.80 | 1.02 |
| 11-03 18:19 | +5 | ZEC | DOWN | 0.67 | 0.76 | 0.61 |
| 11-03 18:18 | +5 | BNB | DOWN | 0.65 | 0.73 | 0.54 |
| 11-03 18:17 | +10 stop | SOL | DOWN | 0.59 | 0.72 | 0.98 |
| 11-03 18:17 | +10 | SOL | DOWN | 0.59 | 0.72 | 0.98 |
| 11-03 18:17 | +10 stop | XRP | DOWN | 0.67 | 0.78 | 0.81 |
| 11-03 18:17 | +20 | XRP | DOWN | 0.67 | 0.87 | 1.76 |
| 11-03 18:17 | +15 | XRP | DOWN | 0.67 | 0.83 | 1.34 |
| 11-03 18:17 | +10 | XRP | DOWN | 0.67 | 0.78 | 0.81 |
| 11-03 18:17 | +5 | XRP | DOWN | 0.67 | 0.78 | 0.81 |
| 11-03 18:17 | +10 stop | BNB | DOWN | 0.61 | 0.73 | 0.89 |
| 11-03 18:17 | +20 | BNB | DOWN | 0.59 | 0.89 | 2.76 |
| 11-03 18:17 | +15 | BNB | DOWN | 0.58 | 0.73 | 1.18 |
| 11-03 18:17 | +10 | BNB | DOWN | 0.58 | 0.69 | 0.77 |
| 11-03 18:17 | +5 | BNB | DOWN | 0.58 | 0.65 | 0.36 |
| 11-03 18:16 | +5 | SOL | DOWN | 0.64 | 0.72 | 0.48 |
| 11-03 18:16 | +10 stop | NEAR | DOWN | 0.61 | 0.72 | 0.78 |
| 11-03 18:16 | +20 | NEAR | DOWN | 0.61 | 0.82 | 1.82 |
| 11-03 18:16 | +15 | NEAR | DOWN | 0.61 | 0.77 | 1.30 |
| 11-03 18:16 | +10 | NEAR | DOWN | 0.61 | 0.72 | 0.78 |
| 11-03 18:16 | +5 | NEAR | DOWN | 0.61 | 0.69 | 0.48 |
| 11-03 18:16 | +10 stop | ETH | DOWN | 0.64 | 0.77 | 1.00 |
| 11-03 18:16 | +20 | ETH | DOWN | 0.64 | 0.84 | 1.73 |
| 11-03 18:16 | +15 | ETH | DOWN | 0.64 | 0.80 | 1.31 |
| 11-03 18:16 | +10 | ETH | DOWN | 0.64 | 0.77 | 1.00 |
