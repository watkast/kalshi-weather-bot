# Range-Scalp Bot

*Updated Mon Oct 12 20:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 13870 | 12007 | 1863 (25) | 4 | $-4392.60 | -5.0% |
| **+10¢** | 10494 | 8324 | 2170 (37) | 4 | $-4154.49 | -6.3% |
| **+15¢** | 8822 | 6502 | 2320 (55) | 5 | $-3682.14 | -6.6% |
| **+20¢** | 7849 | 5432 | 2417 (70) | 5 | $-3136.32 | -6.4% |
| **+10¢ (15¢ stop)** | 17028 | 16981 | 47 (27) | 1 | $-6641.14 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-12 20:07 | +5 | ZEC | UP | 0.62 | open |  |
| 10-12 20:06 | +10 stop | ZEC | UP | 0.59 | open |  |
| 10-12 20:06 | +5 | ZEC | UP | 0.59 | 0.66 | 0.37 |
| 10-12 20:04 | +10 stop | XRP | UP | 0.71 | 0.82 | 0.84 |
| 10-12 20:04 | +10 stop | ETH | UP | 0.70 | 0.83 | 1.05 |
| 10-12 20:04 | +10 | ETH | UP | 0.70 | 0.83 | 1.05 |
| 10-12 20:04 | +5 | ETH | UP | 0.70 | 0.77 | 0.42 |
| 10-12 20:03 | +10 stop | BTC | UP | 0.67 | 0.83 | 1.34 |
| 10-12 20:03 | +20 | BTC | UP | 0.67 | 0.95 | 2.57 |
| 10-12 20:03 | +15 | BTC | UP | 0.67 | 0.83 | 1.34 |
| 10-12 20:03 | +10 | BTC | UP | 0.67 | 0.83 | 1.34 |
| 10-12 20:03 | +5 | BTC | UP | 0.67 | 0.75 | 0.50 |
| 10-12 20:03 | +5 | ZEC | UP | 0.55 | 0.67 | 0.86 |
| 10-12 20:03 | +10 stop | BNB | UP | 0.65 | 0.77 | 0.91 |
| 10-12 20:03 | +10 | BNB | UP | 0.65 | 0.77 | 0.91 |
| 10-12 20:03 | +5 | BNB | UP | 0.65 | 0.73 | 0.50 |
| 10-12 20:03 | +5 | ZEC | DOWN | 0.34 | 0.59 | 2.17 |
| 10-12 20:03 | +10 stop | BNB | DOWN | 0.37 | 0.55 | 1.45 |
| 10-12 20:03 | +10 | BNB | DOWN | 0.37 | 0.55 | 1.45 |
| 10-12 20:03 | +5 | BNB | DOWN | 0.37 | 0.55 | 1.45 |
| 10-12 20:02 | +10 stop | SOL | UP | 0.71 | 0.86 | 1.26 |
| 10-12 20:02 | +10 | SOL | UP | 0.71 | 0.86 | 1.26 |
| 10-12 20:02 | +5 | SOL | UP | 0.71 | 0.78 | 0.42 |
| 10-12 20:02 | +10 stop | ZEC | DOWN | 0.52 | 0.32 | -2.36 |
| 10-12 20:02 | +20 | ZEC | DOWN | 0.52 | open |  |
| 10-12 20:02 | +15 | ZEC | DOWN | 0.52 | open |  |
| 10-12 20:02 | +10 | ZEC | DOWN | 0.53 | open |  |
| 10-12 20:02 | +5 | ZEC | DOWN | 0.53 | 0.58 | 0.14 |
| 10-12 20:01 | +10 stop | XRP | DOWN | 0.56 | 0.40 | -1.95 |
| 10-12 20:01 | +20 | XRP | DOWN | 0.56 | open |  |
| 10-12 20:01 | +15 | XRP | DOWN | 0.56 | open |  |
| 10-12 20:01 | +10 | XRP | DOWN | 0.56 | open |  |
| 10-12 20:01 | +5 | XRP | DOWN | 0.56 | open |  |
| 10-12 20:01 | +10 stop | BNB | DOWN | 0.46 | 0.57 | 0.74 |
| 10-12 20:01 | +20 | BNB | DOWN | 0.46 | open |  |
| 10-12 20:01 | +15 | BNB | DOWN | 0.46 | open |  |
| 10-12 20:01 | +10 | BNB | DOWN | 0.46 | 0.57 | 0.74 |
| 10-12 20:01 | +5 | BNB | DOWN | 0.46 | 0.54 | 0.44 |
| 10-12 20:01 | +10 stop | ETH | UP | 0.63 | 0.74 | 0.83 |
| 10-12 20:01 | +20 | ETH | UP | 0.63 | 0.83 | 1.77 |
