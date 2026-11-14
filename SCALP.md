# Range-Scalp Bot

*Updated Sat Nov 14 11:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59389 | 51826 | 7563 (107) | 2 | $-15991.00 | -4.3% |
| **+10¢** | 44359 | 35506 | 8853 (142) | 2 | $-15000.24 | -5.4% |
| **+15¢** | 37175 | 27627 | 9548 (178) | 1 | $-13635.88 | -5.8% |
| **+20¢** | 33117 | 23095 | 10022 (230) | 1 | $-12011.60 | -5.8% |
| **+10¢ (15¢ stop)** | 72258 | 72116 | 142 (82) | 0 | $-26572.54 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 11:28 | +10 stop | BTC | UP | 0.22 | 0.54 | 2.89 |
| 11-14 11:27 | +10 stop | BTC | UP | 0.58 | 0.42 | -1.96 |
| 11-14 11:27 | +10 | BTC | UP | 0.58 | open |  |
| 11-14 11:27 | +5 | BTC | UP | 0.58 | open |  |
| 11-14 11:25 | +10 stop | BTC | DOWN | 0.58 | 0.70 | 0.87 |
| 11-14 11:25 | +10 stop | SOL | DOWN | 0.64 | 0.81 | 1.42 |
| 11-14 11:24 | +10 stop | BTC | UP | 0.62 | 0.46 | -1.95 |
| 11-14 11:23 | +10 stop | HYPE | DOWN | 0.61 | 0.81 | 1.72 |
| 11-14 11:23 | +5 | HYPE | DOWN | 0.61 | 0.66 | 0.17 |
| 11-14 11:23 | +10 stop | NEAR | DOWN | 0.67 | 0.83 | 1.34 |
| 11-14 11:22 | +10 stop | SOL | UP | 0.64 | 0.47 | -2.05 |
| 11-14 11:21 | +10 stop | BNB | DOWN | 0.59 | 0.74 | 1.19 |
| 11-14 11:21 | +10 stop | BTC | UP | 0.70 | 0.55 | -1.83 |
| 11-14 11:20 | +10 stop | ZEC | UP | 0.50 | 0.25 | -2.82 |
| 11-14 11:20 | +10 stop | DOGE | UP | 0.68 | 0.52 | -1.94 |
| 11-14 11:19 | +5 | BNB | DOWN | 0.66 | 0.74 | 0.50 |
| 11-14 11:18 | +10 stop | HYPE | UP | 0.64 | 0.85 | 1.84 |
| 11-14 11:18 | +5 | HYPE | UP | 0.64 | 0.70 | 0.28 |
| 11-14 11:17 | +10 stop | BTC | UP | 0.59 | 0.83 | 2.13 |
| 11-14 11:17 | +10 stop | BNB | DOWN | 0.61 | 0.46 | -1.85 |
| 11-14 11:17 | +20 | BNB | DOWN | 0.61 | 0.86 | 2.24 |
| 11-14 11:17 | +15 | BNB | DOWN | 0.61 | 0.77 | 1.30 |
| 11-14 11:17 | +10 | BNB | DOWN | 0.61 | 0.74 | 0.99 |
| 11-14 11:17 | +5 | BNB | DOWN | 0.61 | 0.66 | 0.17 |
| 11-14 11:17 | +10 stop | NEAR | UP | 0.58 | 0.38 | -2.35 |
| 11-14 11:17 | +10 stop | ETH | UP | 0.63 | 0.85 | 1.94 |
| 11-14 11:17 | +10 stop | XRP | UP | 0.61 | 0.73 | 0.89 |
| 11-14 11:17 | +10 stop | DOGE | UP | 0.64 | 0.46 | -2.15 |
| 11-14 11:17 | +10 stop | SOL | UP | 0.62 | 0.72 | 0.68 |
| 11-14 11:17 | +10 stop | HYPE | DOWN | 0.58 | 0.43 | -1.86 |
| 11-14 11:17 | +10 | HYPE | DOWN | 0.57 | 0.81 | 2.11 |
| 11-14 11:17 | +5 | HYPE | DOWN | 0.57 | 0.62 | 0.15 |
| 11-14 11:16 | +10 stop | BTC | DOWN | 0.60 | 0.42 | -2.15 |
| 11-14 11:16 | +20 | BTC | DOWN | 0.60 | 0.85 | 2.24 |
| 11-14 11:16 | +15 | BTC | DOWN | 0.60 | 0.85 | 2.24 |
| 11-14 11:16 | +10 | BTC | DOWN | 0.60 | 0.70 | 0.68 |
| 11-14 11:16 | +5 | BTC | DOWN | 0.60 | 0.70 | 0.68 |
| 11-14 11:16 | +10 stop | ETH | DOWN | 0.59 | 0.35 | -2.73 |
| 11-14 11:16 | +20 | ETH | DOWN | 0.59 | open |  |
| 11-14 11:16 | +15 | ETH | DOWN | 0.60 | open |  |
