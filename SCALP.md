# Range-Scalp Bot

*Updated Tue Nov 24 10:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70807 | 61808 | 8999 (148) | 7 | $-18899.25 | -4.2% |
| **+10¢** | 52819 | 42310 | 10509 (193) | 7 | $-17500.56 | -5.3% |
| **+15¢** | 44246 | 32927 | 11319 (250) | 8 | $-15570.53 | -5.6% |
| **+20¢** | 39396 | 27479 | 11917 (316) | 8 | $-13938.56 | -5.6% |
| **+10¢ (15¢ stop)** | 86209 | 86011 | 198 (118) | 4 | $-31689.76 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 10:07 | +10 | ZEC | UP | 0.62 | open |  |
| 11-24 10:07 | +5 | ZEC | UP | 0.62 | open |  |
| 11-24 10:07 | +10 stop | XRP | UP | 0.61 | open |  |
| 11-24 10:06 | +10 stop | ZEC | UP | 0.71 | open |  |
| 11-24 10:06 | +5 | ZEC | UP | 0.70 | 0.78 | 0.52 |
| 11-24 10:06 | +10 stop | SOL | UP | 0.66 | open |  |
| 11-24 10:06 | +10 stop | DOGE | UP | 0.70 | 0.55 | -1.83 |
| 11-24 10:06 | +10 stop | BNB | UP | 0.61 | 0.80 | 1.61 |
| 11-24 10:06 | +10 stop | BTC | UP | 0.62 | 0.74 | 0.89 |
| 11-24 10:05 | +10 stop | HYPE | UP | 0.67 | 0.84 | 1.40 |
| 11-24 10:05 | +10 stop | ETH | UP | 0.69 | 0.80 | 0.83 |
| 11-24 10:05 | +10 stop | NEAR | DOWN | 0.71 | open |  |
| 11-24 10:05 | +10 | NEAR | DOWN | 0.71 | open |  |
| 11-24 10:05 | +5 | NEAR | DOWN | 0.71 | open |  |
| 11-24 10:05 | +5 | XRP | DOWN | 0.60 | open |  |
| 11-24 10:04 | +10 stop | BNB | DOWN | 0.61 | 0.42 | -2.25 |
| 11-24 10:04 | +5 | BNB | DOWN | 0.61 | open |  |
| 11-24 10:03 | +10 stop | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 11-24 10:03 | +20 | NEAR | DOWN | 0.68 | open |  |
| 11-24 10:03 | +15 | NEAR | DOWN | 0.68 | open |  |
| 11-24 10:03 | +10 | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 11-24 10:03 | +5 | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 11-24 10:03 | +10 stop | XRP | DOWN | 0.68 | 0.44 | -2.74 |
| 11-24 10:03 | +15 | XRP | DOWN | 0.68 | open |  |
| 11-24 10:03 | +10 | XRP | DOWN | 0.68 | open |  |
| 11-24 10:03 | +5 | XRP | DOWN | 0.68 | 0.75 | 0.40 |
| 11-24 10:03 | +10 stop | ZEC | UP | 0.54 | 0.71 | 1.37 |
| 11-24 10:03 | +10 stop | HYPE | DOWN | 0.60 | 0.42 | -2.15 |
| 11-24 10:03 | +15 | HYPE | DOWN | 0.60 | open |  |
| 11-24 10:03 | +10 | HYPE | DOWN | 0.60 | open |  |
| 11-24 10:03 | +5 | HYPE | DOWN | 0.60 | open |  |
| 11-24 10:02 | +10 stop | DOGE | DOWN | 0.69 | 0.54 | -1.83 |
| 11-24 10:02 | +20 | DOGE | DOWN | 0.69 | open |  |
| 11-24 10:02 | +15 | DOGE | DOWN | 0.68 | open |  |
| 11-24 10:02 | +10 | DOGE | DOWN | 0.68 | open |  |
| 11-24 10:02 | +5 | DOGE | DOWN | 0.69 | open |  |
| 11-24 10:02 | +10 stop | ETH | DOWN | 0.54 | 0.33 | -2.44 |
| 11-24 10:02 | +10 stop | BTC | DOWN | 0.55 | 0.40 | -1.85 |
| 11-24 10:02 | +10 stop | BNB | DOWN | 0.51 | 0.61 | 0.65 |
| 11-24 10:02 | +20 | BNB | DOWN | 0.51 | open |  |
