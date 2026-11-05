# Range-Scalp Bot

*Updated Thu Nov 05 18:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48709 | 42455 | 6254 (73) | 3 | $-13772.03 | -4.5% |
| **+10¢** | 36352 | 29082 | 7270 (99) | 5 | $-12642.33 | -5.5% |
| **+15¢** | 30440 | 22612 | 7828 (127) | 5 | $-11529.57 | -6.0% |
| **+20¢** | 27040 | 18838 | 8202 (166) | 5 | $-10181.87 | -6.0% |
| **+10¢ (15¢ stop)** | 59357 | 59264 | 93 (56) | 1 | $-21989.53 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 18:12 | +10 stop | XRP | UP | 0.66 | open |  |
| 11-05 18:11 | +5 | HYPE | UP | 0.65 | 0.73 | 0.50 |
| 11-05 18:11 | +10 stop | HYPE | UP | 0.56 | 0.66 | 0.66 |
| 11-05 18:11 | +10 stop | XRP | DOWN | 0.65 | 0.32 | -3.66 |
| 11-05 18:11 | +20 | XRP | DOWN | 0.65 | open |  |
| 11-05 18:11 | +15 | XRP | DOWN | 0.67 | open |  |
| 11-05 18:11 | +10 | XRP | DOWN | 0.67 | open |  |
| 11-05 18:11 | +5 | XRP | DOWN | 0.67 | open |  |
| 11-05 18:11 | +5 | HYPE | UP | 0.49 | 0.57 | 0.44 |
| 11-05 18:10 | +10 stop | DOGE | UP | 0.67 | 0.80 | 1.02 |
| 11-05 18:10 | +20 | DOGE | UP | 0.68 | 0.90 | 1.97 |
| 11-05 18:10 | +15 | DOGE | UP | 0.68 | 0.90 | 1.97 |
| 11-05 18:10 | +10 | DOGE | UP | 0.68 | 0.80 | 0.92 |
| 11-05 18:10 | +5 | DOGE | UP | 0.68 | 0.80 | 0.92 |
| 11-05 18:10 | +5 | HYPE | DOWN | 0.52 | 0.65 | 1.01 |
| 11-05 18:09 | +10 stop | HYPE | DOWN | 0.68 | 0.45 | -2.64 |
| 11-05 18:09 | +15 | HYPE | DOWN | 0.68 | open |  |
| 11-05 18:09 | +10 | HYPE | DOWN | 0.67 | open |  |
| 11-05 18:09 | +5 | HYPE | DOWN | 0.66 | 0.72 | 0.29 |
| 11-05 18:09 | +10 stop | SOL | DOWN | 0.69 | 0.50 | -2.23 |
| 11-05 18:09 | +20 | SOL | DOWN | 0.71 | open |  |
| 11-05 18:09 | +15 | SOL | DOWN | 0.71 | open |  |
| 11-05 18:09 | +10 | SOL | DOWN | 0.71 | open |  |
| 11-05 18:09 | +5 | SOL | DOWN | 0.71 | open |  |
| 11-05 18:09 | +10 stop | BTC | DOWN | 0.68 | 0.39 | -3.23 |
| 11-05 18:09 | +15 | BTC | DOWN | 0.67 | open |  |
| 11-05 18:09 | +10 | BTC | DOWN | 0.67 | open |  |
| 11-05 18:09 | +5 | BTC | DOWN | 0.67 | 0.76 | 0.61 |
| 11-05 18:09 | +10 stop | HYPE | UP | 0.44 | 0.60 | 1.25 |
| 11-05 18:09 | +15 | HYPE | UP | 0.45 | 0.60 | 1.20 |
| 11-05 18:09 | +10 | HYPE | UP | 0.45 | 0.60 | 1.20 |
| 11-05 18:09 | +5 | HYPE | UP | 0.45 | 0.60 | 1.20 |
| 11-05 18:06 | +15 | SOL | DOWN | 0.71 | 0.86 | 1.26 |
| 11-05 18:06 | +5 | SOL | DOWN | 0.71 | 0.80 | 0.63 |
| 11-05 18:04 | +10 stop | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 11-05 18:04 | +10 | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 11-05 18:04 | +5 | SOL | DOWN | 0.70 | 0.75 | 0.21 |
| 11-05 18:03 | +5 | HYPE | DOWN | 0.65 | 0.72 | 0.43 |
| 11-05 18:03 | +10 stop | XRP | DOWN | 0.68 | 0.78 | 0.74 |
| 11-05 18:03 | +5 | XRP | DOWN | 0.66 | 0.71 | 0.19 |
