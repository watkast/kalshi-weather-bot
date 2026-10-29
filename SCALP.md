# Range-Scalp Bot

*Updated Thu Oct 29 00:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38708 | 33775 | 4933 (49) | 0 | $-10893.13 | -4.5% |
| **+10¢** | 28870 | 23174 | 5696 (71) | 0 | $-9658.97 | -5.3% |
| **+15¢** | 24148 | 18028 | 6120 (97) | 0 | $-8621.07 | -5.7% |
| **+20¢** | 21426 | 15018 | 6408 (125) | 1 | $-7512.67 | -5.6% |
| **+10¢ (15¢ stop)** | 47350 | 47283 | 67 (35) | 0 | $-17997.51 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 00:19 | +10 stop | XRP | DOWN | 0.67 | 0.77 | 0.71 |
| 10-29 00:19 | +10 | XRP | DOWN | 0.67 | 0.77 | 0.71 |
| 10-29 00:18 | +5 | XRP | DOWN | 0.67 | 0.73 | 0.30 |
| 10-29 00:17 | +10 stop | DOGE | DOWN | 0.65 | 0.50 | -1.84 |
| 10-29 00:17 | +10 stop | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 10-29 00:17 | +20 | NEAR | DOWN | 0.68 | 0.90 | 1.99 |
| 10-29 00:17 | +15 | NEAR | DOWN | 0.68 | 0.87 | 1.66 |
| 10-29 00:17 | +10 | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 10-29 00:17 | +5 | NEAR | DOWN | 0.68 | 0.73 | 0.20 |
| 10-29 00:16 | +10 stop | HYPE | DOWN | 0.69 | 0.82 | 1.00 |
| 10-29 00:16 | +20 | HYPE | DOWN | 0.69 | 0.96 | 2.46 |
| 10-29 00:16 | +15 | HYPE | DOWN | 0.69 | 0.85 | 1.32 |
| 10-29 00:16 | +10 | HYPE | DOWN | 0.70 | 0.82 | 0.94 |
| 10-29 00:16 | +5 | HYPE | DOWN | 0.69 | 0.75 | 0.27 |
| 10-29 00:16 | +10 stop | BNB | DOWN | 0.62 | 0.84 | 1.93 |
| 10-29 00:16 | +20 | BNB | DOWN | 0.62 | 0.84 | 1.93 |
| 10-29 00:16 | +15 | BNB | DOWN | 0.62 | 0.84 | 1.93 |
| 10-29 00:16 | +10 | BNB | DOWN | 0.62 | 0.84 | 1.93 |
| 10-29 00:16 | +5 | BNB | DOWN | 0.62 | 0.71 | 0.58 |
| 10-29 00:16 | +10 stop | XRP | DOWN | 0.61 | 0.71 | 0.68 |
| 10-29 00:16 | +20 | XRP | DOWN | 0.61 | 0.85 | 2.14 |
| 10-29 00:16 | +15 | XRP | DOWN | 0.61 | 0.77 | 1.30 |
| 10-29 00:16 | +10 | XRP | DOWN | 0.61 | 0.71 | 0.68 |
| 10-29 00:16 | +5 | XRP | DOWN | 0.61 | 0.66 | 0.17 |
| 10-29 00:16 | +10 stop | ETH | DOWN | 0.67 | 0.83 | 1.34 |
| 10-29 00:16 | +20 | ETH | DOWN | 0.67 | 0.87 | 1.76 |
| 10-29 00:16 | +15 | ETH | DOWN | 0.67 | 0.83 | 1.34 |
| 10-29 00:16 | +10 | ETH | DOWN | 0.67 | 0.83 | 1.34 |
| 10-29 00:16 | +5 | ETH | DOWN | 0.67 | 0.73 | 0.30 |
| 10-29 00:16 | +10 stop | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 10-29 00:16 | +20 | BTC | DOWN | 0.65 | 0.89 | 2.17 |
| 10-29 00:16 | +15 | BTC | DOWN | 0.65 | 0.81 | 1.33 |
| 10-29 00:16 | +10 | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 10-29 00:16 | +5 | BTC | DOWN | 0.65 | 0.70 | 0.19 |
| 10-29 00:16 | +10 stop | SOL | DOWN | 0.69 | 0.81 | 0.94 |
| 10-29 00:16 | +20 | SOL | DOWN | 0.68 | 0.88 | 1.76 |
| 10-29 00:16 | +15 | SOL | DOWN | 0.69 | 0.87 | 1.57 |
| 10-29 00:16 | +10 | SOL | DOWN | 0.69 | 0.81 | 0.94 |
| 10-29 00:16 | +5 | SOL | DOWN | 0.69 | 0.76 | 0.42 |
| 10-29 00:15 | +10 stop | DOGE | DOWN | 0.70 | 0.55 | -1.83 |
