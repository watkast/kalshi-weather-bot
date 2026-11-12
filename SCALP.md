# Range-Scalp Bot

*Updated Thu Nov 12 23:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57449 | 50096 | 7353 (101) | 0 | $-15698.73 | -4.3% |
| **+10¢** | 42943 | 34358 | 8585 (133) | 0 | $-14638.10 | -5.4% |
| **+15¢** | 36005 | 26766 | 9239 (167) | 0 | $-13197.43 | -5.8% |
| **+20¢** | 32079 | 22386 | 9693 (217) | 1 | $-11545.80 | -5.7% |
| **+10¢ (15¢ stop)** | 70058 | 69930 | 128 (78) | 0 | $-25829.69 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 23:21 | +10 stop | HYPE | DOWN | 0.62 | 0.76 | 1.05 |
| 11-12 23:21 | +10 | HYPE | DOWN | 0.62 | 0.76 | 1.05 |
| 11-12 23:21 | +5 | HYPE | DOWN | 0.62 | 0.71 | 0.53 |
| 11-12 23:21 | +10 stop | DOGE | DOWN | 0.71 | 0.85 | 1.16 |
| 11-12 23:21 | +15 | DOGE | DOWN | 0.71 | 0.90 | 1.68 |
| 11-12 23:21 | +10 | DOGE | DOWN | 0.71 | 0.85 | 1.16 |
| 11-12 23:21 | +5 | DOGE | DOWN | 0.70 | 0.85 | 1.26 |
| 11-12 23:18 | +5 | ETH | DOWN | 0.66 | 0.71 | 0.19 |
| 11-12 23:18 | +5 | HYPE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-12 23:18 | +5 | XRP | DOWN | 0.68 | 0.81 | 1.03 |
| 11-12 23:17 | +10 stop | DOGE | DOWN | 0.64 | 0.77 | 1.00 |
| 11-12 23:17 | +10 | DOGE | DOWN | 0.64 | 0.77 | 1.00 |
| 11-12 23:17 | +5 | DOGE | DOWN | 0.64 | 0.73 | 0.59 |
| 11-12 23:16 | +10 stop | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 11-12 23:16 | +20 | ETH | DOWN | 0.65 | 0.88 | 2.06 |
| 11-12 23:16 | +15 | ETH | DOWN | 0.65 | 0.84 | 1.64 |
| 11-12 23:16 | +10 | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 11-12 23:16 | +5 | ETH | DOWN | 0.65 | 0.71 | 0.29 |
| 11-12 23:16 | +10 stop | BTC | DOWN | 0.71 | 0.82 | 0.84 |
| 11-12 23:16 | +20 | BTC | DOWN | 0.71 | 0.95 | 2.17 |
| 11-12 23:16 | +15 | BTC | DOWN | 0.71 | 0.87 | 1.37 |
| 11-12 23:16 | +10 | BTC | DOWN | 0.71 | 0.82 | 0.84 |
| 11-12 23:16 | +5 | BTC | DOWN | 0.71 | 0.76 | 0.22 |
| 11-12 23:16 | +10 stop | HYPE | DOWN | 0.71 | 0.83 | 0.95 |
| 11-12 23:16 | +20 | HYPE | DOWN | 0.71 | open |  |
| 11-12 23:16 | +15 | HYPE | DOWN | 0.71 | 0.89 | 1.58 |
| 11-12 23:16 | +10 | HYPE | DOWN | 0.71 | 0.83 | 0.95 |
| 11-12 23:16 | +5 | HYPE | DOWN | 0.71 | 0.76 | 0.22 |
| 11-12 23:16 | +10 stop | BNB | DOWN | 0.64 | 0.81 | 1.38 |
| 11-12 23:16 | +20 | BNB | DOWN | 0.64 | 0.85 | 1.80 |
| 11-12 23:16 | +15 | BNB | DOWN | 0.64 | 0.81 | 1.38 |
| 11-12 23:16 | +10 | BNB | DOWN | 0.65 | 0.81 | 1.36 |
| 11-12 23:16 | +5 | BNB | DOWN | 0.66 | 0.81 | 1.28 |
| 11-12 23:16 | +10 stop | NEAR | DOWN | 0.70 | 0.81 | 0.84 |
| 11-12 23:16 | +20 | NEAR | DOWN | 0.70 | 0.90 | 1.80 |
| 11-12 23:16 | +15 | NEAR | DOWN | 0.70 | 0.85 | 1.26 |
| 11-12 23:16 | +10 | NEAR | DOWN | 0.70 | 0.81 | 0.84 |
| 11-12 23:16 | +5 | NEAR | DOWN | 0.70 | 0.75 | 0.21 |
| 11-12 23:16 | +10 stop | XRP | DOWN | 0.65 | 0.81 | 1.33 |
| 11-12 23:16 | +20 | XRP | DOWN | 0.64 | 0.87 | 2.05 |
