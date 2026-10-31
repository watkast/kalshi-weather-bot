# Range-Scalp Bot

*Updated Sat Oct 31 05:32 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 41824 | 36492 | 5332 (54) | 2 | $-11753.43 | -4.5% |
| **+10¢** | 31177 | 25004 | 6173 (78) | 2 | $-10515.91 | -5.4% |
| **+15¢** | 26062 | 19407 | 6655 (106) | 2 | $-9604.04 | -5.9% |
| **+20¢** | 23142 | 16174 | 6968 (137) | 2 | $-8450.19 | -5.8% |
| **+10¢ (15¢ stop)** | 50983 | 50908 | 75 (41) | 2 | $-19233.64 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 05:31 | +10 stop | BNB | DOWN | 0.70 | open |  |
| 10-31 05:31 | +20 | BNB | DOWN | 0.70 | open |  |
| 10-31 05:31 | +15 | BNB | DOWN | 0.70 | open |  |
| 10-31 05:31 | +10 | BNB | DOWN | 0.70 | open |  |
| 10-31 05:31 | +5 | BNB | DOWN | 0.70 | open |  |
| 10-31 05:30 | +10 stop | XRP | DOWN | 0.66 | open |  |
| 10-31 05:30 | +20 | XRP | DOWN | 0.66 | open |  |
| 10-31 05:30 | +15 | XRP | DOWN | 0.67 | open |  |
| 10-31 05:30 | +10 | XRP | DOWN | 0.66 | open |  |
| 10-31 05:30 | +5 | XRP | DOWN | 0.66 | open |  |
| 10-31 05:28 | +10 stop | DOGE | DOWN | 0.65 | 0.37 | -3.13 |
| 10-31 05:27 | +10 stop | DOGE | DOWN | 0.67 | 0.52 | -1.84 |
| 10-31 05:27 | +20 | DOGE | DOWN | 0.67 | yes | -6.86 |
| 10-31 05:27 | +15 | DOGE | DOWN | 0.67 | yes | -6.86 |
| 10-31 05:27 | +10 | DOGE | DOWN | 0.67 | yes | -6.86 |
| 10-31 05:27 | +5 | DOGE | DOWN | 0.67 | yes | -6.86 |
| 10-31 05:26 | +10 stop | HYPE | DOWN | 0.59 | 0.38 | -2.44 |
| 10-31 05:26 | +15 | HYPE | DOWN | 0.59 | yes | -6.07 |
| 10-31 05:26 | +10 | HYPE | DOWN | 0.59 | yes | -6.07 |
| 10-31 05:26 | +5 | HYPE | DOWN | 0.59 | yes | -6.07 |
| 10-31 05:25 | +10 stop | XRP | UP | 0.67 | 0.91 | 2.19 |
| 10-31 05:25 | +10 stop | HYPE | DOWN | 0.58 | 0.72 | 1.07 |
| 10-31 05:25 | +20 | HYPE | DOWN | 0.59 | yes | -6.04 |
| 10-31 05:25 | +15 | HYPE | DOWN | 0.60 | 0.75 | 1.19 |
| 10-31 05:25 | +10 | HYPE | DOWN | 0.60 | 0.72 | 0.88 |
| 10-31 05:25 | +5 | HYPE | DOWN | 0.60 | 0.72 | 0.88 |
| 10-31 05:25 | +10 stop | ZEC | DOWN | 0.62 | 0.74 | 0.89 |
| 10-31 05:25 | +20 | ZEC | DOWN | 0.62 | 0.86 | 2.14 |
| 10-31 05:25 | +15 | ZEC | DOWN | 0.62 | 0.86 | 2.14 |
| 10-31 05:25 | +10 | ZEC | DOWN | 0.62 | 0.74 | 0.89 |
| 10-31 05:25 | +5 | ZEC | DOWN | 0.62 | 0.74 | 0.89 |
| 10-31 05:23 | +10 stop | XRP | UP | 0.56 | 0.69 | 0.93 |
| 10-31 05:23 | +10 stop | SOL | UP | 0.67 | 0.85 | 1.55 |
| 10-31 05:23 | +20 | SOL | UP | 0.67 | 0.88 | 1.86 |
| 10-31 05:23 | +15 | SOL | UP | 0.67 | 0.85 | 1.55 |
| 10-31 05:23 | +10 | SOL | UP | 0.67 | 0.85 | 1.55 |
| 10-31 05:23 | +5 | SOL | UP | 0.67 | 0.74 | 0.40 |
| 10-31 05:20 | +5 | ETH | UP | 0.68 | 0.75 | 0.40 |
| 10-31 05:20 | +10 stop | ETH | UP | 0.60 | 0.70 | 0.68 |
| 10-31 05:20 | +5 | ETH | UP | 0.60 | 0.65 | 0.17 |
