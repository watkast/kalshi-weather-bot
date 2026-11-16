# Range-Scalp Bot

*Updated Mon Nov 16 00:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61425 | 53598 | 7827 (115) | 1 | $-16534.86 | -4.3% |
| **+10¢** | 45876 | 36703 | 9173 (156) | 0 | $-15525.87 | -5.4% |
| **+15¢** | 38434 | 28537 | 9897 (195) | 0 | $-14180.49 | -5.9% |
| **+20¢** | 34258 | 23876 | 10382 (247) | 0 | $-12449.60 | -5.8% |
| **+10¢ (15¢ stop)** | 74749 | 74595 | 154 (90) | 0 | $-27497.93 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 00:07 | +5 | BNB | DOWN | 0.71 | 0.77 | 0.32 |
| 11-16 00:06 | +10 stop | BNB | DOWN | 0.71 | 0.82 | 0.84 |
| 11-16 00:05 | +10 stop | ETH | UP | 0.52 | 0.37 | -1.85 |
| 11-16 00:05 | +10 stop | BTC | UP | 0.52 | 0.62 | 0.65 |
| 11-16 00:05 | +10 stop | BNB | UP | 0.67 | 0.51 | -1.94 |
| 11-16 00:05 | +5 | BTC | UP | 0.61 | open |  |
| 11-16 00:04 | +10 stop | DOGE | DOWN | 0.66 | 0.76 | 0.71 |
| 11-16 00:04 | +15 | DOGE | DOWN | 0.66 | 0.81 | 1.23 |
| 11-16 00:04 | +10 | DOGE | DOWN | 0.66 | 0.76 | 0.71 |
| 11-16 00:04 | +5 | DOGE | DOWN | 0.66 | 0.76 | 0.71 |
| 11-16 00:04 | +10 stop | SOL | DOWN | 0.67 | 0.79 | 0.92 |
| 11-16 00:04 | +20 | SOL | DOWN | 0.68 | 0.90 | 1.97 |
| 11-16 00:04 | +15 | SOL | DOWN | 0.68 | 0.86 | 1.55 |
| 11-16 00:04 | +10 | SOL | DOWN | 0.68 | 0.79 | 0.82 |
| 11-16 00:04 | +5 | SOL | DOWN | 0.68 | 0.73 | 0.20 |
| 11-16 00:04 | +5 | NEAR | DOWN | 0.69 | 0.75 | 0.31 |
| 11-16 00:04 | +10 stop | BTC | DOWN | 0.56 | 0.39 | -2.05 |
| 11-16 00:04 | +20 | BTC | DOWN | 0.56 | 0.78 | 1.89 |
| 11-16 00:04 | +15 | BTC | DOWN | 0.57 | 0.72 | 1.17 |
| 11-16 00:04 | +10 | BTC | DOWN | 0.57 | 0.72 | 1.17 |
| 11-16 00:04 | +5 | BTC | DOWN | 0.57 | 0.63 | 0.25 |
| 11-16 00:04 | +10 stop | ZEC | DOWN | 0.65 | 0.50 | -1.84 |
| 11-16 00:04 | +20 | ZEC | DOWN | 0.65 | 0.87 | 1.96 |
| 11-16 00:04 | +15 | ZEC | DOWN | 0.65 | 0.80 | 1.22 |
| 11-16 00:04 | +10 | ZEC | DOWN | 0.65 | 0.80 | 1.22 |
| 11-16 00:04 | +5 | ZEC | DOWN | 0.65 | 0.80 | 1.22 |
| 11-16 00:03 | +10 stop | ETH | DOWN | 0.65 | 0.44 | -2.44 |
| 11-16 00:03 | +10 | ETH | DOWN | 0.65 | 0.78 | 1.01 |
| 11-16 00:03 | +5 | ETH | DOWN | 0.65 | 0.78 | 1.01 |
| 11-16 00:03 | +10 stop | BNB | DOWN | 0.60 | 0.43 | -2.05 |
| 11-16 00:03 | +15 | BNB | DOWN | 0.60 | 0.77 | 1.40 |
| 11-16 00:03 | +10 | BNB | DOWN | 0.60 | 0.72 | 0.88 |
| 11-16 00:03 | +5 | BNB | DOWN | 0.60 | 0.66 | 0.27 |
| 11-16 00:02 | +5 | BNB | DOWN | 0.59 | 0.70 | 0.78 |
| 11-16 00:02 | +10 stop | BTC | DOWN | 0.60 | 0.75 | 1.19 |
| 11-16 00:02 | +10 | BTC | DOWN | 0.60 | 0.75 | 1.19 |
| 11-16 00:02 | +5 | BNB | DOWN | 0.53 | 0.61 | 0.45 |
| 11-16 00:02 | +10 stop | ETH | DOWN | 0.59 | 0.71 | 0.88 |
| 11-16 00:02 | +20 | ETH | DOWN | 0.59 | 0.86 | 2.44 |
| 11-16 00:02 | +15 | ETH | DOWN | 0.59 | 0.78 | 1.60 |
