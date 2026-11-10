# Range-Scalp Bot

*Updated Tue Nov 10 13:32 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54545 | 47578 | 6967 (91) | 0 | $-14856.27 | -4.3% |
| **+10¢** | 40750 | 32618 | 8132 (121) | 0 | $-13807.23 | -5.4% |
| **+15¢** | 34159 | 25391 | 8768 (155) | 0 | $-12577.24 | -5.9% |
| **+20¢** | 30419 | 21222 | 9197 (204) | 0 | $-10974.82 | -5.8% |
| **+10¢ (15¢ stop)** | 66462 | 66348 | 114 (70) | 0 | $-24573.81 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 13:24 | +5 | ETH | DOWN | 0.63 | 0.87 | 2.15 |
| 11-10 13:24 | +10 stop | HYPE | DOWN | 0.55 | 0.88 | 3.04 |
| 11-10 13:24 | +5 | ETH | DOWN | 0.57 | 0.65 | 0.46 |
| 11-10 13:24 | +10 stop | NEAR | DOWN | 0.70 | 0.86 | 1.36 |
| 11-10 13:23 | +10 stop | BNB | DOWN | 0.69 | 0.96 | 2.53 |
| 11-10 13:23 | +5 | ZEC | DOWN | 0.68 | 0.79 | 0.77 |
| 11-10 13:22 | +5 | NEAR | DOWN | 0.65 | 0.71 | 0.29 |
| 11-10 13:22 | +10 stop | ETH | DOWN | 0.64 | 0.87 | 2.05 |
| 11-10 13:22 | +20 | ETH | DOWN | 0.64 | 0.87 | 2.05 |
| 11-10 13:22 | +15 | ETH | DOWN | 0.64 | 0.87 | 2.09 |
| 11-10 13:22 | +10 | ETH | DOWN | 0.64 | 0.87 | 2.07 |
| 11-10 13:22 | +5 | ETH | DOWN | 0.64 | 0.71 | 0.40 |
| 11-10 13:21 | +10 stop | HYPE | UP | 0.60 | 0.44 | -1.95 |
| 11-10 13:21 | +10 stop | BNB | DOWN | 0.58 | 0.68 | 0.66 |
| 11-10 13:21 | +10 stop | NEAR | DOWN | 0.53 | 0.67 | 1.06 |
| 11-10 13:21 | +20 | NEAR | DOWN | 0.53 | 0.74 | 1.78 |
| 11-10 13:21 | +15 | NEAR | DOWN | 0.53 | 0.71 | 1.47 |
| 11-10 13:21 | +10 | NEAR | DOWN | 0.53 | 0.67 | 1.06 |
| 11-10 13:21 | +5 | NEAR | DOWN | 0.53 | 0.60 | 0.35 |
| 11-10 13:21 | +5 | ZEC | DOWN | 0.65 | 0.70 | 0.19 |
| 11-10 13:20 | +10 stop | BNB | DOWN | 0.71 | 0.53 | -2.13 |
| 11-10 13:20 | +20 | BNB | DOWN | 0.71 | 0.96 | 2.33 |
| 11-10 13:20 | +15 | BNB | DOWN | 0.71 | 0.96 | 2.33 |
| 11-10 13:20 | +10 | BNB | DOWN | 0.71 | 0.96 | 2.33 |
| 11-10 13:20 | +5 | BNB | DOWN | 0.71 | 0.96 | 2.33 |
| 11-10 13:20 | +10 stop | ZEC | DOWN | 0.65 | 0.79 | 1.12 |
| 11-10 13:20 | +20 | ZEC | DOWN | 0.65 | 0.92 | 2.43 |
| 11-10 13:20 | +15 | ZEC | DOWN | 0.66 | 0.92 | 2.33 |
| 11-10 13:20 | +10 | ZEC | DOWN | 0.66 | 0.79 | 1.02 |
| 11-10 13:20 | +5 | ZEC | DOWN | 0.65 | 0.70 | 0.19 |
| 11-10 13:19 | +10 stop | HYPE | DOWN | 0.66 | 0.37 | -3.23 |
| 11-10 13:19 | +20 | HYPE | DOWN | 0.66 | 0.88 | 1.96 |
| 11-10 13:19 | +15 | HYPE | DOWN | 0.66 | 0.88 | 1.96 |
| 11-10 13:19 | +10 | HYPE | DOWN | 0.66 | 0.88 | 1.96 |
| 11-10 13:19 | +5 | HYPE | DOWN | 0.66 | 0.88 | 1.96 |
| 11-10 13:15 | +10 stop | XRP | DOWN | 0.65 | 0.76 | 0.81 |
| 11-10 13:15 | +20 | XRP | DOWN | 0.65 | 0.85 | 1.75 |
| 11-10 13:15 | +15 | XRP | DOWN | 0.67 | 0.83 | 1.34 |
| 11-10 13:15 | +10 | XRP | DOWN | 0.67 | 0.83 | 1.34 |
| 11-10 13:15 | +5 | XRP | DOWN | 0.67 | 0.76 | 0.61 |
