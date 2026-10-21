# Range-Scalp Bot

*Updated Wed Oct 21 10:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27030 | 23535 | 3495 (39) | 3 | $-7871.17 | -4.6% |
| **+10¢** | 20336 | 16299 | 4037 (55) | 4 | $-6953.44 | -5.4% |
| **+15¢** | 17022 | 12676 | 4346 (78) | 6 | $-6237.99 | -5.8% |
| **+20¢** | 15073 | 10518 | 4555 (97) | 7 | $-5599.70 | -5.9% |
| **+10¢ (15¢ stop)** | 33159 | 33100 | 59 (32) | 2 | $-12276.78 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 10:02 | +10 stop | BTC | DOWN | 0.58 | open |  |
| 10-21 10:02 | +10 stop | ZEC | DOWN | 0.70 | open |  |
| 10-21 10:02 | +20 | ZEC | DOWN | 0.70 | open |  |
| 10-21 10:02 | +15 | ZEC | DOWN | 0.70 | open |  |
| 10-21 10:02 | +10 | ZEC | DOWN | 0.70 | open |  |
| 10-21 10:02 | +5 | ZEC | DOWN | 0.70 | 0.75 | 0.21 |
| 10-21 10:02 | +10 stop | ETH | DOWN | 0.63 | 0.77 | 1.10 |
| 10-21 10:02 | +5 | HYPE | DOWN | 0.66 | 0.71 | 0.19 |
| 10-21 10:02 | +10 stop | DOGE | DOWN | 0.56 | 0.66 | 0.66 |
| 10-21 10:02 | +20 | DOGE | DOWN | 0.55 | open |  |
| 10-21 10:02 | +15 | DOGE | DOWN | 0.55 | 0.72 | 1.37 |
| 10-21 10:02 | +10 | DOGE | DOWN | 0.55 | 0.66 | 0.76 |
| 10-21 10:02 | +5 | DOGE | DOWN | 0.55 | 0.66 | 0.76 |
| 10-21 10:01 | +10 | NEAR | DOWN | 0.69 | 0.81 | 0.94 |
| 10-21 10:01 | +5 | NEAR | DOWN | 0.69 | 0.81 | 0.94 |
| 10-21 10:01 | +10 stop | NEAR | DOWN | 0.71 | 0.81 | 0.74 |
| 10-21 10:01 | +20 | NEAR | DOWN | 0.71 | open |  |
| 10-21 10:01 | +15 | NEAR | DOWN | 0.71 | open |  |
| 10-21 10:01 | +10 stop | HYPE | DOWN | 0.57 | 0.68 | 0.72 |
| 10-21 10:01 | +20 | HYPE | DOWN | 0.57 | open |  |
| 10-21 10:01 | +15 | HYPE | DOWN | 0.57 | open |  |
| 10-21 10:01 | +10 | HYPE | DOWN | 0.57 | 0.68 | 0.72 |
| 10-21 10:01 | +5 | HYPE | DOWN | 0.57 | 0.64 | 0.31 |
| 10-21 10:01 | +10 stop | XRP | UP | 0.67 | 0.49 | -2.14 |
| 10-21 10:01 | +20 | XRP | UP | 0.67 | open |  |
| 10-21 10:01 | +15 | XRP | UP | 0.67 | open |  |
| 10-21 10:01 | +10 | XRP | UP | 0.67 | open |  |
| 10-21 10:01 | +5 | XRP | UP | 0.67 | open |  |
| 10-21 10:01 | +10 stop | BNB | DOWN | 0.61 | 0.72 | 0.78 |
| 10-21 10:01 | +20 | BNB | DOWN | 0.61 | 0.86 | 2.24 |
| 10-21 10:01 | +15 | BNB | DOWN | 0.60 | 0.77 | 1.40 |
| 10-21 10:01 | +10 | BNB | DOWN | 0.60 | 0.72 | 0.88 |
| 10-21 10:01 | +5 | BNB | DOWN | 0.60 | 0.67 | 0.37 |
| 10-21 10:01 | +10 stop | SOL | DOWN | 0.59 | 0.72 | 0.98 |
| 10-21 10:01 | +20 | SOL | DOWN | 0.59 | 0.81 | 1.92 |
| 10-21 10:01 | +15 | SOL | DOWN | 0.59 | 0.77 | 1.50 |
| 10-21 10:01 | +10 | SOL | DOWN | 0.59 | 0.72 | 0.98 |
| 10-21 10:01 | +5 | SOL | DOWN | 0.59 | 0.67 | 0.47 |
| 10-21 10:01 | +10 stop | ETH | UP | 0.58 | 0.41 | -2.05 |
| 10-21 10:01 | +20 | ETH | UP | 0.58 | open |  |
