# Range-Scalp Bot

*Updated Fri Oct 16 07:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 18865 | 16387 | 2478 (28) | 0 | $-5723.77 | -4.8% |
| **+10¢** | 14207 | 11338 | 2869 (40) | 0 | $-5214.88 | -5.8% |
| **+15¢** | 11905 | 8819 | 3086 (59) | 0 | $-4713.77 | -6.3% |
| **+20¢** | 10574 | 7344 | 3230 (78) | 0 | $-4144.17 | -6.2% |
| **+10¢ (15¢ stop)** | 23214 | 23164 | 50 (29) | 0 | $-8971.60 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 07:28 | +10 stop | XRP | UP | 0.32 | 0.53 | 1.76 |
| 10-16 07:28 | +10 stop | BTC | UP | 0.64 | 0.76 | 0.90 |
| 10-16 07:28 | +5 | BTC | UP | 0.66 | 0.76 | 0.71 |
| 10-16 07:27 | +10 stop | XRP | UP | 0.68 | 0.53 | -1.84 |
| 10-16 07:27 | +5 | XRP | UP | 0.66 | 0.98 | 2.97 |
| 10-16 07:26 | +10 stop | BNB | DOWN | 0.65 | 0.49 | -1.94 |
| 10-16 07:26 | +20 | BNB | DOWN | 0.65 | 0.86 | 1.85 |
| 10-16 07:26 | +15 | BNB | DOWN | 0.65 | 0.84 | 1.64 |
| 10-16 07:26 | +10 | BNB | DOWN | 0.65 | 0.84 | 1.64 |
| 10-16 07:26 | +5 | BNB | DOWN | 0.65 | 0.73 | 0.50 |
| 10-16 07:26 | +5 | XRP | DOWN | 0.58 | 0.64 | 0.24 |
| 10-16 07:26 | +10 stop | BTC | DOWN | 0.57 | 0.19 | -4.09 |
| 10-16 07:26 | +10 | BTC | DOWN | 0.57 | yes | -5.88 |
| 10-16 07:26 | +5 | BTC | DOWN | 0.57 | 0.64 | 0.35 |
| 10-16 07:26 | +10 stop | ETH | UP | 0.60 | 0.86 | 2.34 |
| 10-16 07:26 | +20 | ETH | UP | 0.60 | 0.86 | 2.34 |
| 10-16 07:26 | +15 | ETH | UP | 0.60 | 0.86 | 2.34 |
| 10-16 07:26 | +10 | ETH | UP | 0.55 | 0.66 | 0.76 |
| 10-16 07:26 | +5 | ETH | UP | 0.55 | 0.66 | 0.76 |
| 10-16 07:25 | +10 stop | XRP | UP | 0.45 | 0.65 | 1.66 |
| 10-16 07:25 | +5 | XRP | UP | 0.46 | 0.54 | 0.45 |
| 10-16 07:25 | +10 stop | NEAR | DOWN | 0.69 | 0.49 | -2.33 |
| 10-16 07:24 | +5 | XRP | UP | 0.38 | 0.58 | 1.65 |
| 10-16 07:24 | +10 stop | BTC | UP | 0.44 | 0.64 | 1.65 |
| 10-16 07:24 | +10 | BTC | UP | 0.44 | 0.64 | 1.65 |
| 10-16 07:24 | +5 | BTC | UP | 0.44 | 0.64 | 1.65 |
| 10-16 07:24 | +10 stop | DOGE | DOWN | 0.65 | 0.82 | 1.43 |
| 10-16 07:24 | +5 | DOGE | DOWN | 0.65 | 0.82 | 1.43 |
| 10-16 07:24 | +10 stop | ZEC | DOWN | 0.57 | 0.68 | 0.76 |
| 10-16 07:24 | +10 | ZEC | DOWN | 0.57 | 0.68 | 0.76 |
| 10-16 07:24 | +5 | ZEC | DOWN | 0.59 | 0.68 | 0.57 |
| 10-16 07:23 | +5 | DOGE | UP | 0.43 | 0.55 | 0.84 |
| 10-16 07:23 | +10 stop | SOL | UP | 0.66 | 0.50 | -1.94 |
| 10-16 07:22 | +10 stop | HYPE | DOWN | 0.59 | 0.76 | 1.40 |
| 10-16 07:22 | +10 stop | NEAR | UP | 0.66 | 0.44 | -2.54 |
| 10-16 07:22 | +20 | NEAR | UP | 0.66 | 0.87 | 1.86 |
| 10-16 07:22 | +15 | NEAR | UP | 0.66 | 0.84 | 1.54 |
| 10-16 07:22 | +10 | NEAR | UP | 0.66 | 0.84 | 1.54 |
| 10-16 07:22 | +10 stop | BTC | UP | 0.69 | 0.79 | 0.73 |
| 10-16 07:22 | +15 | BTC | UP | 0.69 | 0.91 | 1.97 |
