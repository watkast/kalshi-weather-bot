# Range-Scalp Bot

*Updated Sat Oct 24 14:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32144 | 28024 | 4120 (40) | 0 | $-9201.50 | -4.5% |
| **+10¢** | 24059 | 19290 | 4769 (58) | 0 | $-8233.75 | -5.4% |
| **+15¢** | 20144 | 15014 | 5130 (81) | 0 | $-7380.35 | -5.8% |
| **+20¢** | 17846 | 12476 | 5370 (103) | 1 | $-6554.66 | -5.8% |
| **+10¢ (15¢ stop)** | 39508 | 39449 | 59 (32) | 0 | $-15149.35 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 14:56 | +10 stop | DOGE | UP | 0.60 | 0.25 | -3.81 |
| 10-24 14:56 | +10 stop | BTC | UP | 0.67 | 0.34 | -3.62 |
| 10-24 14:55 | +10 stop | BTC | UP | 0.58 | 0.69 | 0.77 |
| 10-24 14:54 | +10 stop | XRP | DOWN | 0.66 | 0.85 | 1.64 |
| 10-24 14:54 | +10 stop | ZEC | DOWN | 0.55 | 0.67 | 0.86 |
| 10-24 14:54 | +10 stop | BNB | DOWN | 0.61 | 0.88 | 2.45 |
| 10-24 14:54 | +10 stop | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-24 14:54 | +10 stop | BNB | UP | 0.39 | 0.54 | 1.15 |
| 10-24 14:53 | +10 stop | SOL | DOWN | 0.67 | 0.82 | 1.23 |
| 10-24 14:53 | +10 stop | ZEC | UP | 0.60 | 0.44 | -1.95 |
| 10-24 14:52 | +10 stop | BNB | UP | 0.70 | 0.54 | -1.93 |
| 10-24 14:52 | +10 stop | NEAR | DOWN | 0.62 | 0.73 | 0.79 |
| 10-24 14:52 | +10 stop | XRP | UP | 0.58 | 0.38 | -2.33 |
| 10-24 14:51 | +10 stop | DOGE | UP | 0.71 | 0.46 | -2.83 |
| 10-24 14:51 | +10 stop | ETH | UP | 0.64 | 0.43 | -2.45 |
| 10-24 14:51 | +10 stop | ZEC | UP | 0.56 | 0.66 | 0.66 |
| 10-24 14:51 | +5 | SOL | DOWN | 0.62 | 0.67 | 0.17 |
| 10-24 14:50 | +10 stop | NEAR | DOWN | 0.70 | 0.55 | -1.83 |
| 10-24 14:50 | +10 | NEAR | DOWN | 0.70 | 0.86 | 1.36 |
| 10-24 14:50 | +10 stop | BTC | UP | 0.68 | 0.83 | 1.24 |
| 10-24 14:49 | +5 | XRP | DOWN | 0.63 | 0.71 | 0.48 |
| 10-24 14:49 | +5 | ZEC | DOWN | 0.60 | 0.67 | 0.37 |
| 10-24 14:49 | +10 stop | ETH | DOWN | 0.64 | 0.46 | -2.15 |
| 10-24 14:49 | +15 | ETH | DOWN | 0.64 | 0.82 | 1.52 |
| 10-24 14:49 | +10 | ETH | DOWN | 0.64 | 0.76 | 0.90 |
| 10-24 14:49 | +5 | ETH | DOWN | 0.64 | 0.70 | 0.28 |
| 10-24 14:48 | +5 | XRP | DOWN | 0.59 | 0.65 | 0.27 |
| 10-24 14:48 | +10 stop | SOL | DOWN | 0.65 | 0.49 | -1.94 |
| 10-24 14:48 | +10 | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 10-24 14:48 | +5 | SOL | DOWN | 0.65 | 0.70 | 0.19 |
| 10-24 14:48 | +5 | NEAR | DOWN | 0.67 | 0.73 | 0.30 |
| 10-24 14:48 | +5 | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 10-24 14:48 | +10 stop | ZEC | DOWN | 0.63 | 0.47 | -1.94 |
| 10-24 14:48 | +20 | ZEC | DOWN | 0.60 | 0.88 | 2.55 |
| 10-24 14:48 | +15 | ZEC | DOWN | 0.60 | 0.88 | 2.55 |
| 10-24 14:48 | +10 | ZEC | DOWN | 0.60 | 0.74 | 1.09 |
| 10-24 14:48 | +5 | ZEC | DOWN | 0.60 | 0.67 | 0.37 |
| 10-24 14:48 | +5 | BNB | DOWN | 0.65 | 0.88 | 2.06 |
| 10-24 14:47 | +10 stop | BTC | DOWN | 0.66 | 0.43 | -2.64 |
| 10-24 14:47 | +20 | BTC | DOWN | 0.66 | open |  |
