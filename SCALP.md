# Range-Scalp Bot

*Updated Mon Nov 16 00:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61442 | 53614 | 7828 (115) | 2 | $-16535.57 | -4.3% |
| **+10¢** | 45889 | 36716 | 9173 (156) | 1 | $-15515.19 | -5.4% |
| **+15¢** | 38443 | 28546 | 9897 (195) | 2 | $-14168.20 | -5.9% |
| **+20¢** | 34265 | 23883 | 10382 (247) | 3 | $-12436.47 | -5.8% |
| **+10¢ (15¢ stop)** | 74764 | 74610 | 154 (90) | 1 | $-27487.75 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 00:24 | +10 stop | BNB | DOWN | 0.58 | 0.68 | 0.66 |
| 11-16 00:24 | +15 | BNB | DOWN | 0.58 | open |  |
| 11-16 00:24 | +10 | BNB | DOWN | 0.58 | 0.68 | 0.66 |
| 11-16 00:23 | +5 | BTC | DOWN | 0.71 | 0.76 | 0.22 |
| 11-16 00:23 | +10 stop | BTC | DOWN | 0.59 | 0.73 | 1.09 |
| 11-16 00:23 | +20 | BTC | DOWN | 0.59 | open |  |
| 11-16 00:23 | +15 | BTC | DOWN | 0.59 | 0.75 | 1.29 |
| 11-16 00:23 | +10 | BTC | DOWN | 0.59 | 0.73 | 1.09 |
| 11-16 00:23 | +5 | BTC | DOWN | 0.59 | 0.65 | 0.27 |
| 11-16 00:22 | +10 stop | ZEC | DOWN | 0.60 | open |  |
| 11-16 00:22 | +5 | BNB | DOWN | 0.71 | open |  |
| 11-16 00:20 | +10 stop | ZEC | UP | 0.66 | 0.49 | -2.04 |
| 11-16 00:20 | +20 | ZEC | UP | 0.66 | open |  |
| 11-16 00:20 | +15 | ZEC | UP | 0.66 | open |  |
| 11-16 00:20 | +10 | ZEC | UP | 0.66 | open |  |
| 11-16 00:20 | +5 | ZEC | UP | 0.66 | open |  |
| 11-16 00:19 | +10 stop | ETH | DOWN | 0.63 | 0.81 | 1.52 |
| 11-16 00:19 | +5 | ETH | DOWN | 0.63 | 0.68 | 0.17 |
| 11-16 00:19 | +5 | SOL | DOWN | 0.69 | 0.78 | 0.62 |
| 11-16 00:19 | +10 stop | BNB | DOWN | 0.56 | 0.68 | 0.86 |
| 11-16 00:19 | +10 | BNB | DOWN | 0.56 | 0.68 | 0.86 |
| 11-16 00:18 | +10 stop | DOGE | DOWN | 0.71 | 0.81 | 0.74 |
| 11-16 00:18 | +10 stop | BTC | DOWN | 0.69 | 0.80 | 0.83 |
| 11-16 00:18 | +5 | BTC | DOWN | 0.68 | 0.75 | 0.40 |
| 11-16 00:18 | +10 | DOGE | DOWN | 0.68 | 0.79 | 0.82 |
| 11-16 00:18 | +10 | BTC | DOWN | 0.70 | 0.80 | 0.73 |
| 11-16 00:17 | +5 | BTC | DOWN | 0.67 | 0.72 | 0.19 |
| 11-16 00:17 | +5 | BNB | DOWN | 0.63 | 0.68 | 0.17 |
| 11-16 00:17 | +5 | DOGE | DOWN | 0.71 | 0.77 | 0.32 |
| 11-16 00:16 | +10 stop | HYPE | DOWN | 0.70 | 0.80 | 0.73 |
| 11-16 00:16 | +20 | HYPE | DOWN | 0.70 | 0.90 | 1.79 |
| 11-16 00:16 | +15 | HYPE | DOWN | 0.70 | 0.89 | 1.68 |
| 11-16 00:16 | +10 | HYPE | DOWN | 0.70 | 0.80 | 0.73 |
| 11-16 00:16 | +5 | HYPE | DOWN | 0.70 | 0.76 | 0.32 |
| 11-16 00:16 | +10 stop | DOGE | DOWN | 0.61 | 0.71 | 0.68 |
| 11-16 00:16 | +20 | DOGE | DOWN | 0.59 | 0.79 | 1.71 |
| 11-16 00:16 | +15 | DOGE | DOWN | 0.59 | 0.77 | 1.50 |
| 11-16 00:16 | +10 | DOGE | DOWN | 0.59 | 0.70 | 0.78 |
| 11-16 00:16 | +5 | DOGE | DOWN | 0.59 | 0.64 | 0.16 |
| 11-16 00:16 | +10 stop | XRP | DOWN | 0.66 | 0.76 | 0.71 |
