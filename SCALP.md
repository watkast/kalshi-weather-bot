# Range-Scalp Bot

*Updated Sat Oct 10 18:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10728 | 9248 | 1480 (22) | 3 | $-3658.56 | -5.4% |
| **+10¢** | 8120 | 6395 | 1725 (36) | 3 | $-3504.67 | -6.9% |
| **+15¢** | 6850 | 5025 | 1825 (52) | 3 | $-2957.21 | -6.9% |
| **+20¢** | 6092 | 4190 | 1902 (66) | 3 | $-2523.95 | -6.6% |
| **+10¢ (15¢ stop)** | 13181 | 13140 | 41 (25) | 0 | $-5248.75 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 18:28 | +10 stop | DOGE | DOWN | 0.62 | 0.90 | 2.59 |
| 10-10 18:28 | +10 | DOGE | DOWN | 0.62 | 0.90 | 2.59 |
| 10-10 18:28 | +5 | DOGE | DOWN | 0.60 | 0.90 | 2.76 |
| 10-10 18:28 | +5 | BNB | DOWN | 0.62 | 0.67 | 0.21 |
| 10-10 18:26 | +10 stop | BNB | DOWN | 0.68 | 0.35 | -3.61 |
| 10-10 18:26 | +10 stop | BNB | DOWN | 0.66 | 0.48 | -2.14 |
| 10-10 18:25 | +10 stop | DOGE | DOWN | 0.69 | 0.82 | 1.04 |
| 10-10 18:25 | +20 | DOGE | DOWN | 0.69 | 0.90 | 1.88 |
| 10-10 18:25 | +15 | DOGE | DOWN | 0.69 | 0.90 | 1.88 |
| 10-10 18:25 | +10 | DOGE | DOWN | 0.69 | 0.82 | 1.04 |
| 10-10 18:25 | +5 | DOGE | DOWN | 0.69 | 0.77 | 0.52 |
| 10-10 18:24 | +10 stop | NEAR | DOWN | 0.58 | 0.71 | 0.97 |
| 10-10 18:24 | +5 | BNB | DOWN | 0.61 | 0.75 | 1.05 |
| 10-10 18:24 | +10 stop | BNB | DOWN | 0.61 | 0.44 | -2.05 |
| 10-10 18:24 | +10 stop | ETH | UP | 0.47 | 0.30 | -2.03 |
| 10-10 18:24 | +5 | ETH | UP | 0.51 | 0.85 | 3.13 |
| 10-10 18:24 | +10 stop | BNB | UP | 0.36 | 0.57 | 1.75 |
| 10-10 18:23 | +10 stop | HYPE | UP | 0.61 | 0.07 | -5.61 |
| 10-10 18:23 | +20 | HYPE | UP | 0.61 | open |  |
| 10-10 18:23 | +15 | HYPE | UP | 0.61 | open |  |
| 10-10 18:23 | +10 | HYPE | UP | 0.61 | open |  |
| 10-10 18:23 | +5 | HYPE | UP | 0.61 | open |  |
| 10-10 18:23 | +10 stop | BNB | DOWN | 0.60 | 0.45 | -1.85 |
| 10-10 18:23 | +5 | BNB | DOWN | 0.55 | 0.63 | 0.45 |
| 10-10 18:22 | +5 | BNB | UP | 0.40 | 0.57 | 1.35 |
| 10-10 18:22 | +10 stop | NEAR | UP | 0.69 | 0.50 | -2.26 |
| 10-10 18:22 | +10 | NEAR | UP | 0.69 | open |  |
| 10-10 18:22 | +5 | NEAR | UP | 0.69 | open |  |
| 10-10 18:22 | +5 | ETH | UP | 0.54 | 0.62 | 0.47 |
| 10-10 18:20 | +10 stop | ETH | UP | 0.71 | 0.51 | -2.33 |
| 10-10 18:20 | +15 | ETH | UP | 0.71 | 0.92 | 1.88 |
| 10-10 18:20 | +10 | ETH | UP | 0.71 | 0.85 | 1.16 |
| 10-10 18:20 | +5 | ETH | UP | 0.71 | 0.77 | 0.32 |
| 10-10 18:19 | +10 stop | BTC | UP | 0.56 | 0.34 | -2.54 |
| 10-10 18:19 | +10 stop | ZEC | DOWN | 0.59 | 0.81 | 1.92 |
| 10-10 18:18 | +5 | ETH | UP | 0.64 | 0.71 | 0.38 |
| 10-10 18:18 | +10 stop | ZEC | DOWN | 0.65 | 0.50 | -1.84 |
| 10-10 18:18 | +20 | ZEC | DOWN | 0.61 | 0.81 | 1.72 |
| 10-10 18:18 | +15 | ZEC | DOWN | 0.61 | 0.81 | 1.72 |
| 10-10 18:18 | +10 | ZEC | DOWN | 0.61 | 0.81 | 1.72 |
