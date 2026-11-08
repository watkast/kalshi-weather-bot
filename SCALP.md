# Range-Scalp Bot

*Updated Sun Nov 08 02:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51874 | 45234 | 6640 (80) | 0 | $-14368.43 | -4.4% |
| **+10¢** | 38715 | 30969 | 7746 (106) | 0 | $-13390.88 | -5.5% |
| **+15¢** | 32419 | 24071 | 8348 (135) | 0 | $-12284.86 | -6.0% |
| **+20¢** | 28843 | 20092 | 8751 (180) | 0 | $-10807.85 | -6.0% |
| **+10¢ (15¢ stop)** | 63172 | 63069 | 103 (61) | 0 | $-23391.18 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 02:38 | +10 stop | ETH | DOWN | 0.57 | 0.73 | 1.28 |
| 11-08 02:38 | +10 | XRP | DOWN | 0.70 | 0.90 | 1.79 |
| 11-08 02:38 | +5 | XRP | DOWN | 0.70 | 0.79 | 0.63 |
| 11-08 02:37 | +10 stop | ETH | DOWN | 0.44 | 0.54 | 0.64 |
| 11-08 02:37 | +10 stop | BNB | DOWN | 0.51 | 0.63 | 0.90 |
| 11-08 02:37 | +10 stop | XRP | DOWN | 0.71 | 0.90 | 1.69 |
| 11-08 02:37 | +10 stop | BNB | UP | 0.58 | 0.43 | -1.86 |
| 11-08 02:35 | +10 stop | NEAR | DOWN | 0.63 | 0.76 | 1.00 |
| 11-08 02:35 | +20 | NEAR | DOWN | 0.63 | 0.86 | 2.04 |
| 11-08 02:35 | +15 | NEAR | DOWN | 0.63 | 0.82 | 1.62 |
| 11-08 02:35 | +10 | NEAR | DOWN | 0.63 | 0.76 | 1.00 |
| 11-08 02:35 | +5 | NEAR | DOWN | 0.63 | 0.68 | 0.17 |
| 11-08 02:35 | +10 stop | BTC | UP | 0.60 | 0.77 | 1.40 |
| 11-08 02:35 | +10 stop | XRP | DOWN | 0.61 | 0.45 | -1.95 |
| 11-08 02:35 | +20 | XRP | DOWN | 0.60 | 0.90 | 2.77 |
| 11-08 02:35 | +15 | XRP | DOWN | 0.60 | 0.79 | 1.61 |
| 11-08 02:35 | +10 | XRP | DOWN | 0.60 | 0.72 | 0.88 |
| 11-08 02:35 | +5 | XRP | DOWN | 0.61 | 0.69 | 0.48 |
| 11-08 02:35 | +10 stop | ETH | DOWN | 0.71 | 0.45 | -2.93 |
| 11-08 02:35 | +20 | ETH | DOWN | 0.71 | 0.92 | 1.87 |
| 11-08 02:35 | +15 | ETH | DOWN | 0.71 | 0.92 | 1.87 |
| 11-08 02:35 | +10 | ETH | DOWN | 0.71 | 0.84 | 1.05 |
| 11-08 02:35 | +5 | ETH | DOWN | 0.71 | 0.84 | 1.05 |
| 11-08 02:34 | +5 | ZEC | DOWN | 0.67 | 0.82 | 1.23 |
| 11-08 02:34 | +10 stop | BNB | DOWN | 0.71 | 0.38 | -3.62 |
| 11-08 02:34 | +20 | BNB | DOWN | 0.71 | 0.97 | 2.38 |
| 11-08 02:34 | +15 | BNB | DOWN | 0.71 | 0.86 | 1.26 |
| 11-08 02:34 | +10 | BNB | DOWN | 0.71 | 0.86 | 1.26 |
| 11-08 02:34 | +5 | BNB | DOWN | 0.71 | 0.80 | 0.63 |
| 11-08 02:33 | +15 | BTC | DOWN | 0.66 | 0.83 | 1.44 |
| 11-08 02:32 | +10 stop | BTC | DOWN | 0.70 | 0.51 | -2.23 |
| 11-08 02:32 | +10 | BTC | DOWN | 0.70 | 0.83 | 1.05 |
| 11-08 02:32 | +5 | BTC | DOWN | 0.69 | 0.78 | 0.62 |
| 11-08 02:32 | +10 stop | ZEC | DOWN | 0.66 | 0.82 | 1.33 |
| 11-08 02:32 | +20 | ZEC | DOWN | 0.66 | 0.88 | 1.96 |
| 11-08 02:32 | +15 | ZEC | DOWN | 0.66 | 0.82 | 1.33 |
| 11-08 02:32 | +10 | ZEC | DOWN | 0.66 | 0.82 | 1.33 |
| 11-08 02:32 | +5 | ZEC | DOWN | 0.66 | 0.72 | 0.29 |
| 11-08 02:31 | +5 | XRP | DOWN | 0.69 | 0.74 | 0.21 |
| 11-08 02:31 | +5 | ETH | DOWN | 0.70 | 0.76 | 0.32 |
