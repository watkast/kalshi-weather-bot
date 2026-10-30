# Range-Scalp Bot

*Updated Fri Oct 30 07:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 40372 | 35248 | 5124 (51) | 1 | $-11204.82 | -4.4% |
| **+10¢** | 30077 | 24149 | 5928 (74) | 2 | $-9967.53 | -5.3% |
| **+15¢** | 25155 | 18778 | 6377 (101) | 0 | $-8953.56 | -5.7% |
| **+20¢** | 22325 | 15640 | 6685 (130) | 0 | $-7874.08 | -5.6% |
| **+10¢ (15¢ stop)** | 49251 | 49181 | 70 (37) | 2 | $-18650.50 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 07:08 | +10 | HYPE | DOWN | 0.65 | open |  |
| 10-30 07:08 | +10 stop | HYPE | DOWN | 0.70 | open |  |
| 10-30 07:07 | +10 stop | BNB | DOWN | 0.70 | open |  |
| 10-30 07:07 | +10 | BNB | DOWN | 0.70 | open |  |
| 10-30 07:07 | +5 | HYPE | UP | 0.62 | open |  |
| 10-30 07:07 | +5 | BNB | DOWN | 0.70 | 0.79 | 0.63 |
| 10-30 07:07 | +10 stop | ETH | DOWN | 0.59 | 0.82 | 2.02 |
| 10-30 07:06 | +10 stop | HYPE | UP | 0.65 | 0.45 | -2.34 |
| 10-30 07:05 | +10 stop | BNB | DOWN | 0.55 | 0.69 | 1.07 |
| 10-30 07:05 | +20 | BNB | DOWN | 0.55 | 0.79 | 2.10 |
| 10-30 07:05 | +15 | BNB | DOWN | 0.55 | 0.71 | 1.27 |
| 10-30 07:05 | +10 | BNB | DOWN | 0.55 | 0.69 | 1.07 |
| 10-30 07:05 | +5 | BNB | DOWN | 0.55 | 0.63 | 0.43 |
| 10-30 07:05 | +10 stop | ETH | DOWN | 0.66 | 0.45 | -2.44 |
| 10-30 07:05 | +10 stop | HYPE | UP | 0.63 | 0.48 | -1.85 |
| 10-30 07:05 | +5 | HYPE | UP | 0.63 | 0.68 | 0.17 |
| 10-30 07:04 | +5 | DOGE | DOWN | 0.71 | 0.83 | 0.97 |
| 10-30 07:03 | +10 stop | ZEC | DOWN | 0.67 | 0.78 | 0.81 |
| 10-30 07:03 | +20 | ZEC | DOWN | 0.67 | 0.89 | 1.97 |
| 10-30 07:03 | +15 | ZEC | DOWN | 0.67 | 0.89 | 1.97 |
| 10-30 07:03 | +10 | ZEC | DOWN | 0.67 | 0.78 | 0.81 |
| 10-30 07:03 | +5 | ZEC | DOWN | 0.67 | 0.73 | 0.30 |
| 10-30 07:03 | +5 | HYPE | UP | 0.60 | 0.68 | 0.47 |
| 10-30 07:03 | +10 stop | ETH | UP | 0.53 | 0.36 | -2.05 |
| 10-30 07:03 | +5 | NEAR | DOWN | 0.66 | 0.76 | 0.71 |
| 10-30 07:02 | +10 stop | DOGE | DOWN | 0.54 | 0.67 | 0.96 |
| 10-30 07:02 | +20 | DOGE | DOWN | 0.54 | 0.75 | 1.78 |
| 10-30 07:02 | +15 | DOGE | DOWN | 0.54 | 0.75 | 1.78 |
| 10-30 07:02 | +10 | DOGE | DOWN | 0.54 | 0.67 | 0.96 |
| 10-30 07:02 | +5 | DOGE | DOWN | 0.54 | 0.60 | 0.25 |
| 10-30 07:01 | +10 stop | HYPE | DOWN | 0.52 | 0.31 | -2.40 |
| 10-30 07:01 | +20 | HYPE | DOWN | 0.52 | 0.72 | 1.70 |
| 10-30 07:01 | +15 | HYPE | DOWN | 0.52 | 0.72 | 1.70 |
| 10-30 07:01 | +10 | HYPE | DOWN | 0.52 | 0.66 | 1.09 |
| 10-30 07:01 | +5 | HYPE | DOWN | 0.52 | 0.61 | 0.58 |
| 10-30 07:01 | +10 stop | NEAR | DOWN | 0.57 | 0.70 | 0.97 |
| 10-30 07:01 | +20 | NEAR | DOWN | 0.57 | 0.79 | 1.90 |
| 10-30 07:01 | +15 | NEAR | DOWN | 0.57 | 0.76 | 1.59 |
| 10-30 07:01 | +10 | NEAR | DOWN | 0.57 | 0.70 | 0.97 |
| 10-30 07:01 | +5 | NEAR | DOWN | 0.57 | 0.64 | 0.35 |
