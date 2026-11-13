# Range-Scalp Bot

*Updated Fri Nov 13 12:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58255 | 50833 | 7422 (102) | 2 | $-15714.53 | -4.3% |
| **+10¢** | 43530 | 34852 | 8678 (134) | 2 | $-14676.02 | -5.4% |
| **+15¢** | 36494 | 27150 | 9344 (169) | 3 | $-13223.42 | -5.8% |
| **+20¢** | 32513 | 22701 | 9812 (220) | 3 | $-11614.07 | -5.7% |
| **+10¢ (15¢ stop)** | 70978 | 70849 | 129 (79) | 2 | $-26101.50 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 12:06 | +10 stop | NEAR | UP | 0.71 | open |  |
| 11-13 12:06 | +20 | NEAR | UP | 0.71 | open |  |
| 11-13 12:06 | +15 | NEAR | UP | 0.71 | open |  |
| 11-13 12:06 | +10 | NEAR | UP | 0.71 | open |  |
| 11-13 12:06 | +10 stop | BNB | DOWN | 0.60 | open |  |
| 11-13 12:05 | +10 stop | BNB | UP | 0.67 | 0.48 | -2.28 |
| 11-13 12:05 | +20 | BNB | UP | 0.67 | open |  |
| 11-13 12:05 | +15 | BNB | UP | 0.67 | open |  |
| 11-13 12:05 | +10 | BNB | UP | 0.68 | open |  |
| 11-13 12:05 | +5 | BNB | UP | 0.68 | open |  |
| 11-13 12:03 | +10 stop | NEAR | DOWN | 0.64 | 0.46 | -2.15 |
| 11-13 12:02 | +5 | NEAR | DOWN | 0.65 | open |  |
| 11-13 12:02 | +10 stop | HYPE | UP | 0.71 | 0.87 | 1.37 |
| 11-13 12:02 | +20 | HYPE | UP | 0.71 | 0.93 | 1.96 |
| 11-13 12:02 | +15 | HYPE | UP | 0.71 | 0.87 | 1.37 |
| 11-13 12:02 | +10 | HYPE | UP | 0.71 | 0.87 | 1.37 |
| 11-13 12:02 | +5 | HYPE | UP | 0.71 | 0.80 | 0.63 |
| 11-13 12:01 | +10 stop | BTC | UP | 0.71 | 0.82 | 0.84 |
| 11-13 12:01 | +20 | BTC | UP | 0.71 | open |  |
| 11-13 12:01 | +15 | BTC | UP | 0.71 | open |  |
| 11-13 12:01 | +10 | BTC | UP | 0.71 | 0.82 | 0.84 |
| 11-13 12:01 | +5 | BTC | UP | 0.71 | 0.78 | 0.42 |
| 11-13 12:01 | +10 stop | SOL | UP | 0.64 | 0.77 | 1.00 |
| 11-13 12:01 | +20 | SOL | UP | 0.64 | 0.85 | 1.84 |
| 11-13 12:01 | +15 | SOL | UP | 0.64 | 0.79 | 1.21 |
| 11-13 12:01 | +10 | SOL | UP | 0.64 | 0.77 | 1.00 |
| 11-13 12:01 | +5 | SOL | UP | 0.64 | 0.73 | 0.59 |
| 11-13 12:01 | +10 stop | NEAR | UP | 0.47 | 0.32 | -1.84 |
| 11-13 12:01 | +20 | NEAR | UP | 0.47 | 0.69 | 1.87 |
| 11-13 12:01 | +15 | NEAR | UP | 0.48 | 0.69 | 1.79 |
| 11-13 12:01 | +10 | NEAR | UP | 0.48 | 0.69 | 1.79 |
| 11-13 12:01 | +5 | NEAR | UP | 0.48 | 0.53 | 0.16 |
| 11-13 11:59 | +15 | DOGE | DOWN | 0.38 | 0.97 | 5.63 |
| 11-13 11:59 | +10 | DOGE | DOWN | 0.36 | 0.53 | 1.35 |
| 11-13 11:59 | +5 | DOGE | DOWN | 0.64 | 0.97 | 3.07 |
| 11-13 11:57 | +5 | HYPE | UP | 0.64 | 0.77 | 1.00 |
| 11-13 11:57 | +10 stop | BTC | DOWN | 0.61 | 0.36 | -2.84 |
| 11-13 11:56 | +10 stop | BTC | DOWN | 0.61 | 0.75 | 1.09 |
| 11-13 11:56 | +10 stop | DOGE | UP | 0.60 | 0.45 | -1.85 |
| 11-13 11:55 | +10 stop | HYPE | DOWN | 0.47 | 0.58 | 0.74 |
