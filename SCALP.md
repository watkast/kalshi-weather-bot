# Range-Scalp Bot

*Updated Sat Oct 31 09:02 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42034 | 36666 | 5368 (55) | 1 | $-11858.86 | -4.5% |
| **+10¢** | 31336 | 25123 | 6213 (79) | 1 | $-10611.53 | -5.4% |
| **+15¢** | 26199 | 19503 | 6696 (107) | 1 | $-9692.14 | -5.9% |
| **+20¢** | 23267 | 16255 | 7012 (138) | 1 | $-8537.49 | -5.8% |
| **+10¢ (15¢ stop)** | 51242 | 51167 | 75 (41) | 1 | $-19338.51 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 09:02 | +10 stop | HYPE | UP | 0.70 | open |  |
| 10-31 09:02 | +20 | HYPE | UP | 0.66 | open |  |
| 10-31 09:02 | +15 | HYPE | UP | 0.66 | open |  |
| 10-31 09:02 | +10 | HYPE | UP | 0.66 | open |  |
| 10-31 09:02 | +5 | HYPE | UP | 0.66 | open |  |
| 10-31 08:55 | +10 stop | NEAR | UP | 0.61 | 0.43 | -2.15 |
| 10-31 08:52 | +10 stop | NEAR | DOWN | 0.61 | 0.41 | -2.34 |
| 10-31 08:52 | +20 | NEAR | DOWN | 0.61 | 0.87 | 2.35 |
| 10-31 08:52 | +15 | NEAR | DOWN | 0.61 | 0.80 | 1.61 |
| 10-31 08:52 | +10 | NEAR | DOWN | 0.61 | 0.72 | 0.78 |
| 10-31 08:52 | +5 | NEAR | DOWN | 0.61 | 0.68 | 0.37 |
| 10-31 08:52 | +10 stop | SOL | UP | 0.70 | 0.85 | 1.26 |
| 10-31 08:52 | +20 | SOL | UP | 0.70 | 0.92 | 1.95 |
| 10-31 08:52 | +15 | SOL | UP | 0.69 | 0.85 | 1.36 |
| 10-31 08:52 | +10 | SOL | UP | 0.71 | 0.85 | 1.16 |
| 10-31 08:52 | +5 | SOL | UP | 0.71 | 0.79 | 0.53 |
| 10-31 08:47 | +10 stop | BTC | UP | 0.71 | 0.85 | 1.16 |
| 10-31 08:47 | +20 | BTC | UP | 0.71 | 0.92 | 1.84 |
| 10-31 08:47 | +15 | BTC | UP | 0.71 | 0.87 | 1.37 |
| 10-31 08:47 | +10 | BTC | UP | 0.71 | 0.85 | 1.16 |
| 10-31 08:47 | +5 | BTC | UP | 0.71 | 0.77 | 0.32 |
| 10-31 08:38 | +10 stop | XRP | DOWN | 0.68 | 0.81 | 1.03 |
| 10-31 08:38 | +15 | XRP | DOWN | 0.69 | 0.86 | 1.47 |
| 10-31 08:38 | +10 | XRP | DOWN | 0.68 | 0.81 | 1.03 |
| 10-31 08:38 | +5 | XRP | DOWN | 0.68 | 0.81 | 1.03 |
| 10-31 08:34 | +10 stop | DOGE | DOWN | 0.59 | 0.69 | 0.68 |
| 10-31 08:34 | +20 | DOGE | DOWN | 0.59 | 0.85 | 2.34 |
| 10-31 08:34 | +15 | DOGE | DOWN | 0.59 | 0.74 | 1.19 |
| 10-31 08:34 | +10 | DOGE | DOWN | 0.59 | 0.69 | 0.68 |
| 10-31 08:34 | +5 | DOGE | DOWN | 0.59 | 0.69 | 0.68 |
| 10-31 08:34 | +10 stop | SOL | DOWN | 0.69 | 0.82 | 1.04 |
| 10-31 08:33 | +10 stop | BNB | DOWN | 0.71 | 0.82 | 0.84 |
| 10-31 08:33 | +20 | BNB | DOWN | 0.71 | 0.95 | 2.20 |
| 10-31 08:33 | +15 | BNB | DOWN | 0.71 | 0.86 | 1.26 |
| 10-31 08:33 | +10 | BNB | DOWN | 0.71 | 0.82 | 0.84 |
| 10-31 08:33 | +5 | BNB | DOWN | 0.71 | 0.78 | 0.42 |
| 10-31 08:32 | +10 stop | ZEC | DOWN | 0.67 | 0.80 | 1.02 |
| 10-31 08:32 | +10 stop | XRP | DOWN | 0.65 | 0.76 | 0.81 |
| 10-31 08:32 | +20 | XRP | DOWN | 0.65 | 0.86 | 1.85 |
| 10-31 08:32 | +15 | XRP | DOWN | 0.64 | 0.80 | 1.31 |
