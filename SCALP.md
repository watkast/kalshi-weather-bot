# Range-Scalp Bot

*Updated Sat Oct 10 10:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10303 | 8882 | 1421 (22) | 5 | $-3519.52 | -5.4% |
| **+10¢** | 7793 | 6139 | 1654 (34) | 6 | $-3366.33 | -6.9% |
| **+15¢** | 6572 | 4820 | 1752 (49) | 7 | $-2847.29 | -6.9% |
| **+20¢** | 5841 | 4017 | 1824 (63) | 7 | $-2419.15 | -6.6% |
| **+10¢ (15¢ stop)** | 12655 | 12618 | 37 (24) | 3 | $-4954.82 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 10:41 | +10 stop | BTC | UP | 0.57 | open |  |
| 10-10 10:41 | +10 stop | BNB | DOWN | 0.67 | open |  |
| 10-10 10:41 | +5 | BNB | DOWN | 0.67 | open |  |
| 10-10 10:41 | +10 stop | SOL | UP | 0.66 | open |  |
| 10-10 10:38 | +10 stop | SOL | DOWN | 0.55 | 0.29 | -2.93 |
| 10-10 10:37 | +10 stop | BNB | DOWN | 0.69 | 0.49 | -2.36 |
| 10-10 10:37 | +20 | BNB | DOWN | 0.69 | open |  |
| 10-10 10:37 | +15 | BNB | DOWN | 0.69 | open |  |
| 10-10 10:37 | +10 | BNB | DOWN | 0.69 | open |  |
| 10-10 10:37 | +5 | BNB | DOWN | 0.69 | 0.77 | 0.51 |
| 10-10 10:37 | +10 stop | NEAR | UP | 0.65 | 0.81 | 1.35 |
| 10-10 10:37 | +5 | NEAR | UP | 0.65 | 0.81 | 1.35 |
| 10-10 10:37 | +10 stop | ZEC | UP | 0.53 | 0.72 | 1.57 |
| 10-10 10:37 | +10 stop | HYPE | DOWN | 0.70 | 0.82 | 0.93 |
| 10-10 10:37 | +10 | HYPE | DOWN | 0.70 | 0.82 | 0.93 |
| 10-10 10:37 | +5 | HYPE | DOWN | 0.70 | 0.79 | 0.62 |
| 10-10 10:37 | +10 stop | DOGE | UP | 0.66 | 0.77 | 0.81 |
| 10-10 10:37 | +20 | DOGE | UP | 0.66 | 0.86 | 1.75 |
| 10-10 10:37 | +15 | DOGE | UP | 0.66 | 0.83 | 1.44 |
| 10-10 10:37 | +10 | DOGE | UP | 0.66 | 0.77 | 0.81 |
| 10-10 10:37 | +5 | DOGE | UP | 0.66 | 0.72 | 0.29 |
| 10-10 10:36 | +10 stop | BTC | UP | 0.69 | 0.54 | -1.83 |
| 10-10 10:36 | +10 stop | SOL | DOWN | 0.55 | 0.39 | -1.95 |
| 10-10 10:35 | +10 stop | SOL | DOWN | 0.71 | 0.51 | -2.33 |
| 10-10 10:35 | +10 | SOL | DOWN | 0.71 | open |  |
| 10-10 10:35 | +5 | SOL | DOWN | 0.71 | open |  |
| 10-10 10:35 | +10 stop | ZEC | DOWN | 0.63 | 0.44 | -2.25 |
| 10-10 10:35 | +10 | ZEC | DOWN | 0.63 | open |  |
| 10-10 10:35 | +5 | ZEC | DOWN | 0.64 | open |  |
| 10-10 10:34 | +10 stop | ETH | UP | 0.70 | 0.81 | 0.84 |
| 10-10 10:34 | +10 stop | HYPE | DOWN | 0.67 | 0.77 | 0.71 |
| 10-10 10:34 | +20 | HYPE | DOWN | 0.67 | 0.90 | 2.07 |
| 10-10 10:34 | +15 | HYPE | DOWN | 0.67 | 0.82 | 1.23 |
| 10-10 10:34 | +10 | HYPE | DOWN | 0.67 | 0.77 | 0.71 |
| 10-10 10:34 | +5 | HYPE | DOWN | 0.67 | 0.77 | 0.71 |
| 10-10 10:34 | +10 stop | BTC | UP | 0.61 | 0.72 | 0.78 |
| 10-10 10:34 | +10 stop | XRP | UP | 0.55 | 0.72 | 1.37 |
| 10-10 10:34 | +10 | XRP | UP | 0.55 | 0.72 | 1.37 |
| 10-10 10:34 | +5 | XRP | UP | 0.55 | 0.63 | 0.45 |
| 10-10 10:34 | +10 stop | SOL | DOWN | 0.62 | 0.74 | 0.85 |
