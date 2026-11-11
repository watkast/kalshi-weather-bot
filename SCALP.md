# Range-Scalp Bot

*Updated Wed Nov 11 07:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55608 | 48498 | 7110 (94) | 1 | $-15177.09 | -4.3% |
| **+10¢** | 41551 | 33256 | 8295 (124) | 1 | $-14112.65 | -5.4% |
| **+15¢** | 34835 | 25889 | 8946 (158) | 1 | $-12883.27 | -5.9% |
| **+20¢** | 31026 | 21641 | 9385 (207) | 1 | $-11267.63 | -5.8% |
| **+10¢ (15¢ stop)** | 67734 | 67616 | 118 (73) | 0 | $-24911.51 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 07:39 | +10 stop | BTC | DOWN | 0.68 | 0.83 | 1.24 |
| 11-11 07:39 | +20 | BTC | DOWN | 0.68 | 0.90 | 1.99 |
| 11-11 07:39 | +15 | BTC | DOWN | 0.68 | 0.83 | 1.24 |
| 11-11 07:39 | +10 | BTC | DOWN | 0.68 | 0.83 | 1.24 |
| 11-11 07:39 | +5 | BTC | DOWN | 0.68 | 0.73 | 0.20 |
| 11-11 07:37 | +10 stop | ZEC | UP | 0.63 | 0.46 | -2.03 |
| 11-11 07:37 | +10 stop | BTC | UP | 0.52 | 0.23 | -3.21 |
| 11-11 07:35 | +10 stop | BTC | DOWN | 0.70 | 0.45 | -2.83 |
| 11-11 07:34 | +10 stop | BTC | DOWN | 0.55 | 0.66 | 0.76 |
| 11-11 07:34 | +5 | NEAR | DOWN | 0.71 | 0.76 | 0.22 |
| 11-11 07:34 | +10 stop | SOL | DOWN | 0.71 | 0.81 | 0.78 |
| 11-11 07:34 | +15 | SOL | DOWN | 0.71 | 0.87 | 1.41 |
| 11-11 07:34 | +10 | SOL | DOWN | 0.71 | 0.81 | 0.78 |
| 11-11 07:34 | +5 | SOL | DOWN | 0.71 | 0.78 | 0.46 |
| 11-11 07:34 | +10 stop | DOGE | DOWN | 0.66 | 0.79 | 1.02 |
| 11-11 07:34 | +5 | DOGE | DOWN | 0.66 | 0.73 | 0.40 |
| 11-11 07:33 | +10 stop | ETH | DOWN | 0.68 | 0.79 | 0.82 |
| 11-11 07:33 | +10 | ETH | DOWN | 0.68 | 0.79 | 0.82 |
| 11-11 07:33 | +5 | ETH | DOWN | 0.68 | 0.79 | 0.82 |
| 11-11 07:33 | +10 stop | BNB | DOWN | 0.68 | 0.79 | 0.82 |
| 11-11 07:33 | +10 | BNB | DOWN | 0.68 | 0.79 | 0.82 |
| 11-11 07:33 | +5 | BNB | DOWN | 0.68 | 0.74 | 0.30 |
| 11-11 07:33 | +10 stop | HYPE | DOWN | 0.65 | 0.75 | 0.70 |
| 11-11 07:33 | +10 | HYPE | DOWN | 0.65 | 0.75 | 0.70 |
| 11-11 07:33 | +5 | HYPE | DOWN | 0.66 | 0.72 | 0.29 |
| 11-11 07:33 | +10 stop | BTC | UP | 0.56 | 0.40 | -1.95 |
| 11-11 07:33 | +10 stop | ZEC | UP | 0.58 | 0.72 | 1.07 |
| 11-11 07:33 | +10 stop | NEAR | DOWN | 0.58 | 0.72 | 1.07 |
| 11-11 07:33 | +10 | NEAR | DOWN | 0.58 | 0.72 | 1.07 |
| 11-11 07:33 | +5 | NEAR | DOWN | 0.58 | 0.64 | 0.25 |
| 11-11 07:32 | +5 | DOGE | DOWN | 0.54 | 0.66 | 0.86 |
| 11-11 07:32 | +10 stop | BNB | DOWN | 0.50 | 0.61 | 0.75 |
| 11-11 07:32 | +10 | BNB | DOWN | 0.50 | 0.61 | 0.75 |
| 11-11 07:32 | +5 | BNB | DOWN | 0.50 | 0.61 | 0.75 |
| 11-11 07:32 | +10 stop | HYPE | DOWN | 0.53 | 0.65 | 0.86 |
| 11-11 07:32 | +20 | HYPE | DOWN | 0.53 | 0.75 | 1.88 |
| 11-11 07:32 | +15 | HYPE | DOWN | 0.53 | 0.72 | 1.57 |
| 11-11 07:32 | +10 | HYPE | DOWN | 0.53 | 0.65 | 0.86 |
| 11-11 07:32 | +5 | HYPE | DOWN | 0.53 | 0.65 | 0.86 |
| 11-11 07:32 | +5 | XRP | DOWN | 0.67 | 0.74 | 0.40 |
