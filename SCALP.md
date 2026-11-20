# Range-Scalp Bot

*Updated Fri Nov 20 22:52 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 66640 | 58157 | 8483 (128) | 1 | $-17935.81 | -4.3% |
| **+10¢** | 49766 | 39851 | 9915 (170) | 1 | $-16676.64 | -5.3% |
| **+15¢** | 41734 | 31043 | 10691 (217) | 1 | $-14993.59 | -5.7% |
| **+20¢** | 37154 | 25927 | 11227 (273) | 2 | $-13268.02 | -5.7% |
| **+10¢ (15¢ stop)** | 81154 | 80988 | 166 (100) | 0 | $-29983.13 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 22:50 | +10 stop | ZEC | UP | 0.59 | 0.72 | 0.98 |
| 11-20 22:49 | +10 stop | ZEC | DOWN | 0.69 | 0.42 | -3.03 |
| 11-20 22:49 | +10 | ZEC | DOWN | 0.69 | open |  |
| 11-20 22:49 | +5 | ZEC | DOWN | 0.69 | open |  |
| 11-20 22:46 | +10 stop | ZEC | DOWN | 0.61 | 0.71 | 0.68 |
| 11-20 22:46 | +20 | ZEC | DOWN | 0.61 | open |  |
| 11-20 22:46 | +15 | ZEC | DOWN | 0.61 | open |  |
| 11-20 22:46 | +10 | ZEC | DOWN | 0.61 | 0.71 | 0.68 |
| 11-20 22:46 | +5 | ZEC | DOWN | 0.61 | 0.70 | 0.58 |
| 11-20 22:46 | +10 stop | HYPE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-20 22:46 | +20 | HYPE | DOWN | 0.64 | 0.84 | 1.73 |
| 11-20 22:46 | +15 | HYPE | DOWN | 0.64 | 0.84 | 1.73 |
| 11-20 22:46 | +10 | HYPE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-20 22:46 | +5 | HYPE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-20 22:46 | +10 stop | BNB | DOWN | 0.71 | 0.86 | 1.26 |
| 11-20 22:46 | +20 | BNB | DOWN | 0.71 | 0.93 | 2.00 |
| 11-20 22:46 | +15 | BNB | DOWN | 0.71 | 0.86 | 1.30 |
| 11-20 22:46 | +10 | BNB | DOWN | 0.71 | 0.86 | 1.26 |
| 11-20 22:46 | +10 stop | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 11-20 22:46 | +20 | XRP | DOWN | 0.70 | 0.91 | 1.88 |
| 11-20 22:46 | +15 | XRP | DOWN | 0.70 | 0.91 | 1.88 |
| 11-20 22:46 | +10 | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 11-20 22:46 | +5 | XRP | DOWN | 0.70 | 0.77 | 0.42 |
| 11-20 22:46 | +10 stop | BTC | DOWN | 0.70 | 0.83 | 1.05 |
| 11-20 22:46 | +20 | BTC | DOWN | 0.70 | 0.92 | 2.04 |
| 11-20 22:46 | +15 | BTC | DOWN | 0.70 | 0.89 | 1.68 |
| 11-20 22:46 | +10 | BTC | DOWN | 0.70 | 0.83 | 1.05 |
| 11-20 22:46 | +5 | BTC | DOWN | 0.70 | 0.83 | 1.05 |
| 11-20 22:46 | +10 stop | DOGE | DOWN | 0.69 | 0.80 | 0.83 |
| 11-20 22:46 | +20 | DOGE | DOWN | 0.69 | 0.90 | 1.89 |
| 11-20 22:46 | +15 | DOGE | DOWN | 0.69 | 0.86 | 1.46 |
| 11-20 22:46 | +10 | DOGE | DOWN | 0.69 | 0.80 | 0.83 |
| 11-20 22:46 | +5 | DOGE | DOWN | 0.69 | 0.80 | 0.83 |
| 11-20 22:46 | +10 stop | NEAR | DOWN | 0.70 | 0.83 | 1.05 |
| 11-20 22:46 | +20 | NEAR | DOWN | 0.70 | open |  |
| 11-20 22:46 | +15 | NEAR | DOWN | 0.70 | 0.86 | 1.36 |
| 11-20 22:46 | +10 | NEAR | DOWN | 0.70 | 0.83 | 1.05 |
| 11-20 22:46 | +5 | NEAR | DOWN | 0.70 | 0.77 | 0.42 |
| 11-20 22:42 | +10 stop | XRP | UP | 0.70 | 0.49 | -2.43 |
| 11-20 22:42 | +10 stop | ETH | UP | 0.68 | 0.82 | 1.13 |
