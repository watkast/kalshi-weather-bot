# Range-Scalp Bot

*Updated Tue Nov 03 00:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45342 | 39477 | 5865 (67) | 0 | $-13126.56 | -4.6% |
| **+10¢** | 33844 | 27049 | 6795 (89) | 0 | $-11996.80 | -5.6% |
| **+15¢** | 28311 | 20999 | 7312 (116) | 0 | $-11049.01 | -6.2% |
| **+20¢** | 25142 | 17484 | 7658 (151) | 0 | $-9818.12 | -6.2% |
| **+10¢ (15¢ stop)** | 55325 | 55238 | 87 (51) | 0 | $-20892.82 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 00:12 | +10 stop | BTC | UP | 0.65 | 0.75 | 0.70 |
| 11-03 00:12 | +10 | BTC | UP | 0.67 | 0.82 | 1.23 |
| 11-03 00:12 | +5 | BTC | UP | 0.65 | 0.75 | 0.70 |
| 11-03 00:11 | +10 stop | BTC | DOWN | 0.49 | 0.61 | 0.85 |
| 11-03 00:11 | +10 stop | BNB | DOWN | 0.44 | 0.58 | 1.04 |
| 11-03 00:11 | +10 stop | XRP | UP | 0.69 | 0.82 | 1.05 |
| 11-03 00:07 | +10 stop | NEAR | UP | 0.66 | 0.77 | 0.81 |
| 11-03 00:07 | +10 stop | BNB | DOWN | 0.60 | 0.81 | 1.82 |
| 11-03 00:06 | +10 stop | XRP | DOWN | 0.70 | 0.82 | 0.94 |
| 11-03 00:05 | +5 | NEAR | DOWN | 0.56 | yes | -5.78 |
| 11-03 00:04 | +10 stop | SOL | UP | 0.62 | 0.47 | -1.85 |
| 11-03 00:04 | +15 | SOL | UP | 0.62 | 0.78 | 1.30 |
| 11-03 00:04 | +10 | SOL | UP | 0.62 | 0.78 | 1.30 |
| 11-03 00:04 | +5 | SOL | UP | 0.62 | 0.69 | 0.38 |
| 11-03 00:04 | +10 stop | BNB | UP | 0.59 | 0.41 | -2.19 |
| 11-03 00:04 | +10 | BNB | UP | 0.59 | 0.86 | 2.39 |
| 11-03 00:04 | +10 stop | DOGE | DOWN | 0.62 | 0.76 | 1.10 |
| 11-03 00:04 | +15 | DOGE | DOWN | 0.62 | 0.83 | 1.83 |
| 11-03 00:04 | +10 | DOGE | DOWN | 0.62 | 0.76 | 1.10 |
| 11-03 00:04 | +5 | DOGE | DOWN | 0.62 | 0.67 | 0.17 |
| 11-03 00:04 | +5 | ZEC | DOWN | 0.64 | yes | -6.57 |
| 11-03 00:04 | +5 | BNB | UP | 0.60 | 0.86 | 2.34 |
| 11-03 00:03 | +10 stop | NEAR | DOWN | 0.60 | 0.43 | -2.05 |
| 11-03 00:03 | +10 | NEAR | DOWN | 0.60 | yes | -6.17 |
| 11-03 00:03 | +5 | NEAR | DOWN | 0.60 | 0.65 | 0.17 |
| 11-03 00:03 | +10 stop | HYPE | UP | 0.63 | 0.76 | 0.99 |
| 11-03 00:03 | +5 | SOL | UP | 0.63 | 0.72 | 0.58 |
| 11-03 00:03 | +10 stop | ETH | DOWN | 0.67 | 0.80 | 1.02 |
| 11-03 00:03 | +10 stop | NEAR | DOWN | 0.54 | 0.66 | 0.86 |
| 11-03 00:03 | +20 | NEAR | DOWN | 0.54 | yes | -5.58 |
| 11-03 00:03 | +15 | NEAR | DOWN | 0.54 | yes | -5.58 |
| 11-03 00:03 | +10 | NEAR | DOWN | 0.54 | 0.66 | 0.86 |
| 11-03 00:03 | +5 | NEAR | DOWN | 0.54 | 0.66 | 0.86 |
| 11-03 00:02 | +10 stop | SOL | UP | 0.53 | 0.64 | 0.75 |
| 11-03 00:02 | +20 | SOL | UP | 0.53 | 0.78 | 2.19 |
| 11-03 00:02 | +15 | SOL | UP | 0.53 | 0.72 | 1.57 |
| 11-03 00:02 | +10 | SOL | UP | 0.53 | 0.64 | 0.75 |
| 11-03 00:02 | +5 | SOL | UP | 0.53 | 0.58 | 0.14 |
| 11-03 00:02 | +10 stop | BNB | UP | 0.48 | 0.60 | 0.85 |
| 11-03 00:02 | +20 | BNB | UP | 0.48 | 0.86 | 3.53 |
