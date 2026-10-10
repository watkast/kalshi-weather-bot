# Range-Scalp Bot

*Updated Sat Oct 10 22:20 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10991 | 9479 | 1512 (22) | 4 | $-3725.36 | -5.4% |
| **+10¢** | 8318 | 6557 | 1761 (36) | 5 | $-3552.98 | -6.8% |
| **+15¢** | 7014 | 5152 | 1862 (52) | 5 | $-2983.59 | -6.8% |
| **+20¢** | 6238 | 4299 | 1939 (66) | 8 | $-2524.01 | -6.4% |
| **+10¢ (15¢ stop)** | 13537 | 13496 | 41 (25) | 2 | $-5440.55 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 22:19 | +5 | ETH | DOWN | 0.60 | open |  |
| 10-10 22:18 | +10 stop | NEAR | DOWN | 0.63 | 0.76 | 1.00 |
| 10-10 22:18 | +20 | NEAR | DOWN | 0.63 | open |  |
| 10-10 22:18 | +15 | NEAR | DOWN | 0.63 | 0.79 | 1.31 |
| 10-10 22:18 | +10 | NEAR | DOWN | 0.63 | 0.76 | 1.00 |
| 10-10 22:18 | +5 | NEAR | DOWN | 0.63 | 0.69 | 0.28 |
| 10-10 22:18 | +5 | HYPE | UP | 0.62 | open |  |
| 10-10 22:18 | +10 stop | SOL | UP | 0.62 | 0.32 | -3.33 |
| 10-10 22:18 | +10 stop | XRP | DOWN | 0.63 | 0.82 | 1.62 |
| 10-10 22:18 | +20 | XRP | DOWN | 0.63 | 0.86 | 2.04 |
| 10-10 22:18 | +15 | XRP | DOWN | 0.63 | 0.82 | 1.62 |
| 10-10 22:18 | +10 | XRP | DOWN | 0.63 | 0.82 | 1.62 |
| 10-10 22:18 | +5 | XRP | DOWN | 0.63 | 0.68 | 0.17 |
| 10-10 22:17 | +5 | BNB | UP | 0.61 | open |  |
| 10-10 22:17 | +10 stop | ETH | DOWN | 0.50 | open |  |
| 10-10 22:17 | +20 | ETH | DOWN | 0.50 | open |  |
| 10-10 22:17 | +15 | ETH | DOWN | 0.50 | open |  |
| 10-10 22:17 | +10 | ETH | DOWN | 0.50 | open |  |
| 10-10 22:17 | +5 | ETH | DOWN | 0.50 | 0.55 | 0.14 |
| 10-10 22:17 | +10 stop | BTC | DOWN | 0.62 | 0.76 | 1.10 |
| 10-10 22:17 | +20 | BTC | DOWN | 0.62 | open |  |
| 10-10 22:17 | +15 | BTC | DOWN | 0.62 | 0.78 | 1.30 |
| 10-10 22:17 | +10 | BTC | DOWN | 0.62 | 0.76 | 1.10 |
| 10-10 22:17 | +5 | BTC | DOWN | 0.62 | 0.69 | 0.38 |
| 10-10 22:17 | +10 stop | BNB | UP | 0.57 | open |  |
| 10-10 22:17 | +20 | BNB | UP | 0.57 | open |  |
| 10-10 22:17 | +15 | BNB | UP | 0.57 | open |  |
| 10-10 22:17 | +10 | BNB | UP | 0.57 | open |  |
| 10-10 22:17 | +5 | BNB | UP | 0.57 | 0.65 | 0.43 |
| 10-10 22:17 | +5 | HYPE | UP | 0.57 | 0.63 | 0.25 |
| 10-10 22:16 | +10 stop | HYPE | UP | 0.56 | 0.36 | -2.35 |
| 10-10 22:16 | +20 | HYPE | UP | 0.56 | open |  |
| 10-10 22:16 | +15 | HYPE | UP | 0.56 | open |  |
| 10-10 22:16 | +10 | HYPE | UP | 0.55 | open |  |
| 10-10 22:16 | +5 | HYPE | UP | 0.55 | 0.63 | 0.45 |
| 10-10 22:16 | +10 stop | ZEC | DOWN | 0.58 | 0.42 | -1.94 |
| 10-10 22:16 | +20 | ZEC | DOWN | 0.58 | open |  |
| 10-10 22:16 | +15 | ZEC | DOWN | 0.58 | open |  |
| 10-10 22:16 | +10 | ZEC | DOWN | 0.58 | open |  |
| 10-10 22:16 | +5 | ZEC | DOWN | 0.58 | 0.65 | 0.36 |
