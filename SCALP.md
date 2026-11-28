# Range-Scalp Bot

*Updated Sat Nov 28 04:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 74346 | 64896 | 9450 (171) | 4 | $-19722.29 | -4.2% |
| **+10¢** | 55382 | 44338 | 11044 (217) | 4 | $-18362.50 | -5.3% |
| **+15¢** | 46372 | 34480 | 11892 (275) | 5 | $-16406.06 | -5.6% |
| **+20¢** | 41264 | 28740 | 12524 (342) | 8 | $-14818.10 | -5.7% |
| **+10¢ (15¢ stop)** | 90475 | 90256 | 219 (135) | 3 | $-33421.77 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-28 04:06 | +10 stop | SOL | DOWN | 0.69 | open |  |
| 11-28 04:06 | +10 | SOL | DOWN | 0.69 | open |  |
| 11-28 04:06 | +5 | SOL | DOWN | 0.69 | open |  |
| 11-28 04:05 | +10 stop | DOGE | UP | 0.65 | open |  |
| 11-28 04:05 | +15 | DOGE | UP | 0.65 | open |  |
| 11-28 04:05 | +10 | DOGE | UP | 0.65 | open |  |
| 11-28 04:05 | +5 | DOGE | UP | 0.65 | open |  |
| 11-28 04:04 | +10 stop | HYPE | UP | 0.56 | 0.70 | 1.03 |
| 11-28 04:04 | +15 | HYPE | UP | 0.56 | 0.81 | 2.16 |
| 11-28 04:04 | +10 | HYPE | UP | 0.57 | 0.70 | 1.01 |
| 11-28 04:04 | +5 | HYPE | UP | 0.57 | 0.64 | 0.39 |
| 11-28 04:04 | +10 stop | NEAR | DOWN | 0.69 | open |  |
| 11-28 04:04 | +10 | NEAR | DOWN | 0.69 | open |  |
| 11-28 04:04 | +5 | NEAR | DOWN | 0.69 | open |  |
| 11-28 04:04 | +5 | HYPE | UP | 0.66 | 0.73 | 0.40 |
| 11-28 04:02 | +10 stop | ZEC | DOWN | 0.68 | 0.41 | -3.01 |
| 11-28 04:02 | +5 | ZEC | DOWN | 0.69 | open |  |
| 11-28 04:02 | +10 stop | BNB | UP | 0.64 | 0.76 | 0.90 |
| 11-28 04:02 | +20 | BNB | UP | 0.64 | open |  |
| 11-28 04:02 | +15 | BNB | UP | 0.64 | 0.81 | 1.42 |
| 11-28 04:02 | +10 | BNB | UP | 0.64 | 0.76 | 0.90 |
| 11-28 04:02 | +5 | BNB | UP | 0.64 | 0.69 | 0.18 |
| 11-28 04:02 | +5 | DOGE | UP | 0.58 | 0.69 | 0.77 |
| 11-28 04:02 | +10 | NEAR | UP | 0.51 | 0.61 | 0.65 |
| 11-28 04:02 | +10 stop | DOGE | UP | 0.63 | 0.73 | 0.69 |
| 11-28 04:02 | +20 | DOGE | UP | 0.63 | open |  |
| 11-28 04:02 | +15 | DOGE | UP | 0.62 | 0.80 | 1.51 |
| 11-28 04:02 | +10 | DOGE | UP | 0.62 | 0.73 | 0.79 |
| 11-28 04:02 | +5 | DOGE | UP | 0.62 | 0.67 | 0.17 |
| 11-28 04:02 | +5 | ETH | UP | 0.65 | 0.72 | 0.43 |
| 11-28 04:02 | +5 | NEAR | UP | 0.51 | 0.61 | 0.65 |
| 11-28 04:01 | +10 stop | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 11-28 04:01 | +20 | SOL | DOWN | 0.65 | open |  |
| 11-28 04:01 | +15 | SOL | DOWN | 0.65 | open |  |
| 11-28 04:01 | +10 | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 11-28 04:01 | +5 | SOL | DOWN | 0.65 | 0.70 | 0.19 |
| 11-28 04:01 | +10 stop | BTC | UP | 0.62 | 0.72 | 0.68 |
| 11-28 04:01 | +20 | BTC | UP | 0.62 | open |  |
| 11-28 04:01 | +15 | BTC | UP | 0.62 | open |  |
| 11-28 04:01 | +10 | BTC | UP | 0.62 | 0.72 | 0.68 |
