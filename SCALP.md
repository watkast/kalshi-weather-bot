# Range-Scalp Bot

*Updated Sat Oct 10 07:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10144 | 8746 | 1398 (18) | 2 | $-3487.08 | -5.4% |
| **+10¢** | 7666 | 6038 | 1628 (30) | 2 | $-3353.08 | -6.9% |
| **+15¢** | 6474 | 4755 | 1719 (43) | 3 | $-2799.54 | -6.9% |
| **+20¢** | 5751 | 3965 | 1786 (56) | 5 | $-2362.80 | -6.5% |
| **+10¢ (15¢ stop)** | 12472 | 12437 | 35 (22) | 0 | $-4896.38 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 07:41 | +10 stop | ETH | DOWN | 0.59 | 0.42 | -2.05 |
| 10-10 07:41 | +10 stop | SOL | UP | 0.67 | 0.83 | 1.34 |
| 10-10 07:41 | +10 stop | BNB | UP | 0.61 | 0.88 | 2.45 |
| 10-10 07:41 | +20 | BNB | UP | 0.61 | 0.88 | 2.45 |
| 10-10 07:41 | +15 | BNB | UP | 0.61 | 0.88 | 2.45 |
| 10-10 07:41 | +10 | BNB | UP | 0.61 | 0.88 | 2.45 |
| 10-10 07:41 | +5 | BNB | UP | 0.61 | 0.88 | 2.41 |
| 10-10 07:40 | +5 | NEAR | UP | 0.71 | 0.79 | 0.53 |
| 10-10 07:40 | +10 stop | XRP | DOWN | 0.64 | 0.33 | -3.43 |
| 10-10 07:40 | +20 | XRP | DOWN | 0.64 | open |  |
| 10-10 07:40 | +15 | XRP | DOWN | 0.64 | open |  |
| 10-10 07:40 | +10 | XRP | DOWN | 0.64 | open |  |
| 10-10 07:40 | +5 | XRP | DOWN | 0.64 | open |  |
| 10-10 07:40 | +10 stop | NEAR | UP | 0.57 | 0.68 | 0.76 |
| 10-10 07:40 | +15 | NEAR | UP | 0.57 | 0.79 | 1.90 |
| 10-10 07:40 | +10 | NEAR | UP | 0.57 | 0.68 | 0.76 |
| 10-10 07:40 | +5 | NEAR | UP | 0.57 | 0.64 | 0.35 |
| 10-10 07:39 | +10 stop | XRP | UP | 0.39 | 0.64 | 2.16 |
| 10-10 07:39 | +20 | XRP | UP | 0.39 | 0.64 | 2.16 |
| 10-10 07:39 | +15 | XRP | UP | 0.39 | 0.64 | 2.16 |
| 10-10 07:39 | +10 | XRP | UP | 0.39 | 0.64 | 2.16 |
| 10-10 07:39 | +5 | XRP | UP | 0.39 | 0.64 | 2.16 |
| 10-10 07:39 | +10 stop | ETH | DOWN | 0.57 | 0.67 | 0.66 |
| 10-10 07:39 | +10 stop | SOL | UP | 0.49 | 0.29 | -2.33 |
| 10-10 07:39 | +20 | SOL | UP | 0.54 | 0.83 | 2.62 |
| 10-10 07:39 | +15 | SOL | UP | 0.54 | 0.83 | 2.62 |
| 10-10 07:39 | +10 | SOL | UP | 0.54 | 0.65 | 0.76 |
| 10-10 07:39 | +5 | SOL | UP | 0.54 | 0.65 | 0.76 |
| 10-10 07:39 | +10 stop | DOGE | UP | 0.49 | 0.59 | 0.65 |
| 10-10 07:39 | +20 | DOGE | UP | 0.49 | open |  |
| 10-10 07:39 | +10 | DOGE | UP | 0.48 | 0.59 | 0.75 |
| 10-10 07:39 | +5 | DOGE | UP | 0.48 | 0.59 | 0.74 |
| 10-10 07:38 | +5 | ETH | UP | 0.65 | open |  |
| 10-10 07:37 | +5 | HYPE | UP | 0.63 | 0.69 | 0.28 |
| 10-10 07:36 | +5 | ZEC | DOWN | 0.71 | 0.77 | 0.32 |
| 10-10 07:36 | +10 | ETH | UP | 0.69 | open |  |
| 10-10 07:36 | +5 | ETH | UP | 0.69 | 0.78 | 0.62 |
| 10-10 07:36 | +10 stop | HYPE | UP | 0.58 | 0.69 | 0.77 |
| 10-10 07:36 | +5 | HYPE | UP | 0.58 | 0.63 | 0.15 |
| 10-10 07:36 | +10 stop | ETH | UP | 0.69 | 0.49 | -2.33 |
