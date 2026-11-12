# Range-Scalp Bot

*Updated Thu Nov 12 01:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56381 | 49155 | 7226 (98) | 0 | $-15482.27 | -4.4% |
| **+10¢** | 42132 | 33702 | 8430 (128) | 2 | $-14440.46 | -5.5% |
| **+15¢** | 35334 | 26250 | 9084 (162) | 2 | $-13130.44 | -5.9% |
| **+20¢** | 31478 | 21948 | 9530 (212) | 5 | $-11488.21 | -5.8% |
| **+10¢ (15¢ stop)** | 68711 | 68588 | 123 (73) | 2 | $-25364.20 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 01:21 | +10 stop | ZEC | DOWN | 0.65 | open |  |
| 11-12 01:20 | +10 stop | SOL | DOWN | 0.71 | open |  |
| 11-12 01:20 | +10 stop | XRP | UP | 0.57 | 0.35 | -2.54 |
| 11-12 01:20 | +10 stop | DOGE | UP | 0.50 | 0.25 | -2.82 |
| 11-12 01:19 | +10 stop | SOL | UP | 0.43 | 0.55 | 0.84 |
| 11-12 01:19 | +10 stop | XRP | UP | 0.52 | 0.67 | 1.16 |
| 11-12 01:19 | +10 stop | ZEC | UP | 0.70 | 0.49 | -2.43 |
| 11-12 01:18 | +10 stop | HYPE | DOWN | 0.52 | 0.64 | 0.85 |
| 11-12 01:18 | +20 | HYPE | DOWN | 0.52 | 0.76 | 2.09 |
| 11-12 01:18 | +15 | HYPE | DOWN | 0.52 | 0.67 | 1.16 |
| 11-12 01:18 | +10 | HYPE | DOWN | 0.52 | 0.64 | 0.85 |
| 11-12 01:18 | +5 | HYPE | DOWN | 0.54 | 0.64 | 0.65 |
| 11-12 01:18 | +10 stop | NEAR | UP | 0.56 | 0.40 | -1.95 |
| 11-12 01:18 | +10 stop | BNB | DOWN | 0.68 | 0.81 | 1.03 |
| 11-12 01:18 | +20 | BNB | DOWN | 0.68 | 0.88 | 1.76 |
| 11-12 01:18 | +15 | BNB | DOWN | 0.68 | 0.86 | 1.55 |
| 11-12 01:18 | +10 | BNB | DOWN | 0.68 | 0.81 | 1.03 |
| 11-12 01:18 | +5 | BNB | DOWN | 0.68 | 0.73 | 0.20 |
| 11-12 01:18 | +5 | SOL | DOWN | 0.67 | 0.76 | 0.61 |
| 11-12 01:18 | +10 stop | XRP | DOWN | 0.63 | 0.47 | -1.95 |
| 11-12 01:17 | +10 stop | DOGE | DOWN | 0.66 | 0.47 | -2.24 |
| 11-12 01:17 | +20 | DOGE | DOWN | 0.66 | open |  |
| 11-12 01:17 | +15 | DOGE | DOWN | 0.66 | 0.81 | 1.23 |
| 11-12 01:17 | +10 | DOGE | DOWN | 0.66 | 0.78 | 0.91 |
| 11-12 01:17 | +5 | DOGE | DOWN | 0.66 | 0.73 | 0.40 |
| 11-12 01:17 | +5 | ETH | DOWN | 0.68 | 0.73 | 0.20 |
| 11-12 01:17 | +5 | SOL | DOWN | 0.59 | 0.64 | 0.16 |
| 11-12 01:16 | +10 stop | SOL | DOWN | 0.63 | 0.45 | -2.15 |
| 11-12 01:16 | +20 | SOL | DOWN | 0.63 | open |  |
| 11-12 01:16 | +15 | SOL | DOWN | 0.63 | 0.80 | 1.41 |
| 11-12 01:16 | +10 | SOL | DOWN | 0.63 | 0.76 | 1.00 |
| 11-12 01:16 | +5 | SOL | DOWN | 0.63 | 0.69 | 0.28 |
| 11-12 01:16 | +10 stop | ETH | DOWN | 0.66 | 0.77 | 0.81 |
| 11-12 01:16 | +20 | ETH | DOWN | 0.66 | 0.91 | 2.25 |
| 11-12 01:16 | +15 | ETH | DOWN | 0.66 | 0.82 | 1.33 |
| 11-12 01:16 | +10 | ETH | DOWN | 0.66 | 0.77 | 0.81 |
| 11-12 01:16 | +5 | ETH | DOWN | 0.68 | 0.73 | 0.20 |
| 11-12 01:16 | +10 | BTC | DOWN | 0.66 | 0.79 | 1.02 |
| 11-12 01:16 | +5 | BTC | DOWN | 0.67 | 0.75 | 0.50 |
| 11-12 01:16 | +10 stop | BTC | DOWN | 0.71 | 0.82 | 0.84 |
