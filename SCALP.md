# Range-Scalp Bot

*Updated Thu Nov 12 11:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56807 | 49517 | 7290 (101) | 4 | $-15660.77 | -4.4% |
| **+10¢** | 42455 | 33952 | 8503 (133) | 4 | $-14578.80 | -5.5% |
| **+15¢** | 35593 | 26440 | 9153 (167) | 5 | $-13214.65 | -5.9% |
| **+20¢** | 31704 | 22100 | 9604 (217) | 5 | $-11606.25 | -5.8% |
| **+10¢ (15¢ stop)** | 69267 | 69139 | 128 (78) | 3 | $-25602.10 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 11:03 | +10 stop | NEAR | DOWN | 0.71 | open |  |
| 11-12 11:03 | +10 | NEAR | DOWN | 0.71 | open |  |
| 11-12 11:03 | +5 | NEAR | DOWN | 0.71 | open |  |
| 11-12 11:02 | +15 | DOGE | UP | 0.63 | open |  |
| 11-12 11:02 | +10 stop | BNB | UP | 0.56 | open |  |
| 11-12 11:02 | +10 | BNB | UP | 0.57 | open |  |
| 11-12 11:02 | +10 stop | DOGE | UP | 0.63 | open |  |
| 11-12 11:02 | +10 | DOGE | UP | 0.63 | open |  |
| 11-12 11:02 | +5 | DOGE | UP | 0.63 | open |  |
| 11-12 11:02 | +5 | BNB | UP | 0.63 | open |  |
| 11-12 11:02 | +10 stop | XRP | UP | 0.60 | 0.39 | -2.44 |
| 11-12 11:02 | +10 | XRP | UP | 0.61 | open |  |
| 11-12 11:02 | +5 | XRP | UP | 0.61 | open |  |
| 11-12 11:01 | +10 stop | DOGE | UP | 0.49 | 0.63 | 1.05 |
| 11-12 11:01 | +20 | DOGE | UP | 0.49 | open |  |
| 11-12 11:01 | +15 | DOGE | UP | 0.49 | 0.64 | 1.15 |
| 11-12 11:01 | +10 | DOGE | UP | 0.49 | 0.63 | 1.05 |
| 11-12 11:01 | +5 | DOGE | UP | 0.49 | 0.63 | 1.05 |
| 11-12 11:01 | +10 stop | XRP | UP | 0.55 | 0.68 | 0.96 |
| 11-12 11:01 | +20 | XRP | UP | 0.55 | open |  |
| 11-12 11:01 | +15 | XRP | UP | 0.55 | open |  |
| 11-12 11:01 | +10 | XRP | UP | 0.55 | 0.68 | 0.96 |
| 11-12 11:01 | +5 | XRP | UP | 0.55 | 0.68 | 0.96 |
| 11-12 11:01 | +10 stop | BNB | UP | 0.54 | 0.64 | 0.65 |
| 11-12 11:01 | +20 | BNB | UP | 0.54 | open |  |
| 11-12 11:01 | +15 | BNB | UP | 0.54 | open |  |
| 11-12 11:01 | +10 | BNB | UP | 0.54 | 0.64 | 0.65 |
| 11-12 11:01 | +5 | BNB | UP | 0.54 | 0.59 | 0.15 |
| 11-12 11:01 | +10 stop | HYPE | UP | 0.60 | 0.74 | 1.06 |
| 11-12 11:01 | +20 | HYPE | UP | 0.60 | open |  |
| 11-12 11:01 | +15 | HYPE | UP | 0.60 | open |  |
| 11-12 11:01 | +10 | HYPE | UP | 0.60 | 0.74 | 1.06 |
| 11-12 11:01 | +5 | HYPE | UP | 0.60 | 0.67 | 0.34 |
| 11-12 11:01 | +10 stop | NEAR | UP | 0.45 | 0.55 | 0.64 |
| 11-12 11:01 | +20 | NEAR | UP | 0.45 | open |  |
| 11-12 11:01 | +15 | NEAR | UP | 0.45 | open |  |
| 11-12 11:01 | +10 | NEAR | UP | 0.45 | 0.55 | 0.64 |
| 11-12 11:01 | +5 | NEAR | UP | 0.45 | 0.55 | 0.64 |
| 11-12 10:57 | +10 stop | ZEC | DOWN | 0.68 | 0.52 | -1.94 |
| 11-12 10:57 | +15 | ZEC | DOWN | 0.65 | 0.95 | 2.81 |
