# Range-Scalp Bot

*Updated Wed Oct 07 10:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 6272 | 5443 | 829 (9) | 0 | $-1895.16 | -4.8% |
| **+10¢** | 4776 | 3802 | 974 (16) | 0 | $-1774.83 | -5.9% |
| **+15¢** | 4015 | 2986 | 1029 (20) | 0 | $-1490.56 | -5.9% |
| **+20¢** | 3591 | 2515 | 1076 (27) | 0 | $-1215.86 | -5.4% |
| **+10¢ (15¢ stop)** | 7605 | 7590 | 15 (9) | 0 | $-2650.33 | -5.6% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 10:31 | +10 stop | BTC | DOWN | 0.67 | 0.80 | 1.02 |
| 10-07 10:31 | +20 | BTC | DOWN | 0.67 | 0.89 | 1.97 |
| 10-07 10:31 | +15 | BTC | DOWN | 0.67 | 0.82 | 1.23 |
| 10-07 10:31 | +10 | BTC | DOWN | 0.67 | 0.80 | 1.02 |
| 10-07 10:31 | +5 | BTC | DOWN | 0.67 | 0.72 | 0.19 |
| 10-07 10:23 | +5 | ZEC | UP | 0.65 | 0.86 | 1.82 |
| 10-07 10:23 | +10 stop | ZEC | UP | 0.64 | 0.86 | 1.94 |
| 10-07 10:21 | +10 stop | XRP | UP | 0.69 | 0.81 | 0.95 |
| 10-07 10:21 | +10 stop | ZEC | DOWN | 0.63 | 0.47 | -1.95 |
| 10-07 10:20 | +10 stop | ZEC | DOWN | 0.57 | 0.72 | 1.17 |
| 10-07 10:19 | +5 | XRP | UP | 0.59 | 0.66 | 0.37 |
| 10-07 10:19 | +10 stop | ETH | UP | 0.63 | 0.74 | 0.79 |
| 10-07 10:19 | +10 | ETH | UP | 0.64 | 0.74 | 0.69 |
| 10-07 10:19 | +5 | XRP | UP | 0.53 | 0.67 | 1.06 |
| 10-07 10:19 | +5 | ETH | UP | 0.69 | 0.74 | 0.21 |
| 10-07 10:19 | +5 | XRP | UP | 0.60 | 0.68 | 0.47 |
| 10-07 10:19 | +10 stop | BNB | UP | 0.59 | 0.69 | 0.68 |
| 10-07 10:18 | +10 stop | XRP | UP | 0.69 | 0.48 | -2.43 |
| 10-07 10:18 | +10 stop | SOL | UP | 0.70 | 0.81 | 0.84 |
| 10-07 10:18 | +10 stop | HYPE | UP | 0.68 | 0.85 | 1.45 |
| 10-07 10:18 | +10 stop | DOGE | UP | 0.60 | 0.70 | 0.68 |
| 10-07 10:17 | +10 stop | BNB | DOWN | 0.58 | 0.38 | -2.34 |
| 10-07 10:17 | +5 | BNB | DOWN | 0.58 | yes | -5.98 |
| 10-07 10:17 | +10 stop | SOL | DOWN | 0.56 | 0.39 | -2.05 |
| 10-07 10:17 | +10 stop | XRP | DOWN | 0.58 | 0.41 | -2.05 |
| 10-07 10:17 | +5 | BNB | DOWN | 0.56 | 0.61 | 0.17 |
| 10-07 10:16 | +5 | NEAR | UP | 0.55 | 0.64 | 0.55 |
| 10-07 10:16 | +10 stop | NEAR | UP | 0.59 | 0.72 | 0.98 |
| 10-07 10:16 | +20 | NEAR | UP | 0.59 | 0.80 | 1.81 |
| 10-07 10:16 | +15 | NEAR | UP | 0.57 | 0.72 | 1.17 |
| 10-07 10:16 | +10 | NEAR | UP | 0.57 | 0.72 | 1.17 |
| 10-07 10:16 | +5 | NEAR | UP | 0.57 | 0.64 | 0.35 |
| 10-07 10:16 | +10 stop | BNB | UP | 0.54 | 0.38 | -1.95 |
| 10-07 10:16 | +20 | BNB | UP | 0.54 | 0.74 | 1.68 |
| 10-07 10:16 | +15 | BNB | UP | 0.54 | 0.69 | 1.17 |
| 10-07 10:16 | +10 | BNB | UP | 0.54 | 0.69 | 1.17 |
| 10-07 10:16 | +5 | BNB | UP | 0.54 | 0.60 | 0.25 |
| 10-07 10:16 | +10 stop | DOGE | UP | 0.69 | 0.49 | -2.33 |
| 10-07 10:16 | +20 | DOGE | UP | 0.69 | 0.89 | 1.78 |
| 10-07 10:16 | +15 | DOGE | UP | 0.69 | 0.88 | 1.67 |
