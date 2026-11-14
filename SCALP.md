# Range-Scalp Bot

*Updated Sat Nov 14 09:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59242 | 51691 | 7551 (107) | 1 | $-15994.03 | -4.3% |
| **+10¢** | 44256 | 35420 | 8836 (140) | 3 | $-15014.12 | -5.4% |
| **+15¢** | 37086 | 27558 | 9528 (176) | 3 | $-13650.36 | -5.9% |
| **+20¢** | 33036 | 23033 | 10003 (228) | 3 | $-12046.52 | -5.8% |
| **+10¢ (15¢ stop)** | 72094 | 71952 | 142 (82) | 0 | $-26503.29 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 09:03 | +10 stop | HYPE | UP | 0.67 | 0.83 | 1.34 |
| 11-14 09:03 | +10 stop | NEAR | UP | 0.59 | 0.69 | 0.68 |
| 11-14 09:03 | +5 | NEAR | UP | 0.58 | 0.69 | 0.77 |
| 11-14 09:02 | +10 stop | NEAR | UP | 0.50 | 0.61 | 0.75 |
| 11-14 09:02 | +5 | NEAR | UP | 0.49 | 0.59 | 0.65 |
| 11-14 09:01 | +5 | NEAR | DOWN | 0.51 | 0.60 | 0.55 |
| 11-14 09:01 | +10 stop | BNB | DOWN | 0.48 | 0.20 | -3.10 |
| 11-14 09:01 | +20 | BNB | DOWN | 0.48 | open |  |
| 11-14 09:01 | +15 | BNB | DOWN | 0.48 | open |  |
| 11-14 09:01 | +10 | BNB | DOWN | 0.48 | open |  |
| 11-14 09:01 | +5 | BNB | DOWN | 0.48 | 0.53 | 0.14 |
| 11-14 09:01 | +10 stop | SOL | UP | 0.53 | 0.82 | 2.61 |
| 11-14 09:01 | +20 | SOL | UP | 0.54 | 0.82 | 2.51 |
| 11-14 09:01 | +15 | SOL | UP | 0.52 | 0.82 | 2.71 |
| 11-14 09:01 | +10 | SOL | UP | 0.52 | 0.82 | 2.71 |
| 11-14 09:01 | +5 | SOL | UP | 0.52 | 0.82 | 2.71 |
| 11-14 09:01 | +10 stop | ZEC | UP | 0.58 | 0.73 | 1.18 |
| 11-14 09:01 | +20 | ZEC | UP | 0.58 | 0.79 | 1.80 |
| 11-14 09:01 | +15 | ZEC | UP | 0.58 | 0.73 | 1.18 |
| 11-14 09:01 | +10 | ZEC | UP | 0.58 | 0.73 | 1.18 |
| 11-14 09:01 | +5 | ZEC | UP | 0.58 | 0.73 | 1.18 |
| 11-14 09:00 | +10 stop | XRP | UP | 0.62 | 0.83 | 1.83 |
| 11-14 09:00 | +20 | XRP | UP | 0.62 | 0.83 | 1.83 |
| 11-14 09:00 | +15 | XRP | UP | 0.62 | 0.83 | 1.83 |
| 11-14 09:00 | +10 | XRP | UP | 0.62 | 0.83 | 1.83 |
| 11-14 09:00 | +5 | XRP | UP | 0.62 | 0.83 | 1.83 |
| 11-14 09:00 | +10 stop | HYPE | DOWN | 0.53 | 0.26 | -3.02 |
| 11-14 09:00 | +20 | HYPE | DOWN | 0.53 | open |  |
| 11-14 09:00 | +15 | HYPE | DOWN | 0.53 | open |  |
| 11-14 09:00 | +10 | HYPE | DOWN | 0.53 | open |  |
| 11-14 09:00 | +5 | HYPE | DOWN | 0.53 | open |  |
| 11-14 09:00 | +10 stop | NEAR | DOWN | 0.56 | 0.36 | -2.37 |
| 11-14 09:00 | +20 | NEAR | DOWN | 0.56 | open |  |
| 11-14 09:00 | +15 | NEAR | DOWN | 0.56 | open |  |
| 11-14 09:00 | +10 | NEAR | DOWN | 0.56 | open |  |
| 11-14 09:00 | +5 | NEAR | DOWN | 0.56 | 0.65 | 0.54 |
| 11-14 08:56 | +10 stop | NEAR | DOWN | 0.61 | 0.39 | -2.54 |
| 11-14 08:54 | +10 stop | NEAR | DOWN | 0.53 | 0.71 | 1.47 |
| 11-14 08:53 | +10 stop | NEAR | DOWN | 0.53 | 0.66 | 0.96 |
| 11-14 08:52 | +5 | NEAR | UP | 0.71 | 0.81 | 0.74 |
