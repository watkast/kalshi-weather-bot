# Range-Scalp Bot

*Updated Wed Nov 11 04:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55385 | 48300 | 7085 (94) | 3 | $-15142.36 | -4.3% |
| **+10¢** | 41370 | 33104 | 8266 (124) | 4 | $-14091.19 | -5.4% |
| **+15¢** | 34684 | 25773 | 8911 (158) | 5 | $-12851.49 | -5.9% |
| **+20¢** | 30884 | 21537 | 9347 (207) | 5 | $-11243.04 | -5.8% |
| **+10¢ (15¢ stop)** | 67446 | 67328 | 118 (73) | 2 | $-24857.99 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 04:07 | +10 stop | XRP | UP | 0.55 | 0.65 | 0.66 |
| 11-11 04:07 | +10 stop | ZEC | DOWN | 0.65 | open |  |
| 11-11 04:07 | +20 | ZEC | DOWN | 0.65 | open |  |
| 11-11 04:07 | +15 | ZEC | DOWN | 0.65 | open |  |
| 11-11 04:07 | +10 | ZEC | DOWN | 0.65 | open |  |
| 11-11 04:07 | +5 | ZEC | DOWN | 0.65 | 0.70 | 0.19 |
| 11-11 04:06 | +10 stop | SOL | UP | 0.59 | open |  |
| 11-11 04:05 | +10 stop | XRP | UP | 0.58 | 0.42 | -1.96 |
| 11-11 04:05 | +20 | XRP | UP | 0.58 | open |  |
| 11-11 04:05 | +15 | XRP | UP | 0.58 | open |  |
| 11-11 04:05 | +10 | XRP | UP | 0.58 | open |  |
| 11-11 04:05 | +10 stop | NEAR | DOWN | 0.60 | 0.72 | 0.88 |
| 11-11 04:05 | +10 stop | ZEC | UP | 0.53 | 0.28 | -2.83 |
| 11-11 04:04 | +5 | ZEC | UP | 0.54 | 0.67 | 0.96 |
| 11-11 04:04 | +10 stop | SOL | UP | 0.64 | 0.75 | 0.79 |
| 11-11 04:02 | +10 stop | ZEC | UP | 0.57 | 0.67 | 0.66 |
| 11-11 04:02 | +5 | ZEC | UP | 0.57 | 0.65 | 0.46 |
| 11-11 04:02 | +10 stop | HYPE | UP | 0.70 | 0.85 | 1.26 |
| 11-11 04:02 | +5 | HYPE | UP | 0.69 | 0.85 | 1.32 |
| 11-11 04:02 | +10 stop | SOL | UP | 0.59 | 0.69 | 0.68 |
| 11-11 04:02 | +10 stop | XRP | DOWN | 0.59 | 0.32 | -3.03 |
| 11-11 04:02 | +5 | BTC | UP | 0.69 | 0.77 | 0.52 |
| 11-11 04:02 | +5 | NEAR | DOWN | 0.57 | 0.72 | 1.17 |
| 11-11 04:01 | +10 stop | XRP | DOWN | 0.54 | 0.66 | 0.86 |
| 11-11 04:01 | +10 stop | ZEC | DOWN | 0.44 | 0.54 | 0.64 |
| 11-11 04:01 | +20 | ZEC | DOWN | 0.48 | 0.71 | 1.97 |
| 11-11 04:01 | +15 | ZEC | DOWN | 0.48 | 0.71 | 1.97 |
| 11-11 04:01 | +10 | ZEC | DOWN | 0.49 | 0.71 | 1.87 |
| 11-11 04:01 | +5 | ZEC | DOWN | 0.49 | 0.54 | 0.14 |
| 11-11 04:01 | +10 stop | SOL | DOWN | 0.52 | 0.37 | -1.85 |
| 11-11 04:01 | +20 | SOL | DOWN | 0.52 | open |  |
| 11-11 04:01 | +15 | SOL | DOWN | 0.52 | open |  |
| 11-11 04:01 | +10 | SOL | DOWN | 0.52 | open |  |
| 11-11 04:01 | +5 | SOL | DOWN | 0.52 | open |  |
| 11-11 04:01 | +5 | XRP | DOWN | 0.66 | open |  |
| 11-11 04:01 | +10 stop | BNB | DOWN | 0.62 | 0.27 | -3.81 |
| 11-11 04:01 | +20 | BNB | DOWN | 0.62 | open |  |
| 11-11 04:01 | +15 | BNB | DOWN | 0.62 | open |  |
| 11-11 04:01 | +10 | BNB | DOWN | 0.62 | open |  |
| 11-11 04:01 | +5 | BNB | DOWN | 0.62 | open |  |
