# Range-Scalp Bot

*Updated Mon Nov 23 12:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69922 | 61018 | 8904 (146) | 3 | $-18797.28 | -4.3% |
| **+10¢** | 52172 | 41768 | 10404 (189) | 5 | $-17492.30 | -5.3% |
| **+15¢** | 43721 | 32514 | 11207 (245) | 6 | $-15604.32 | -5.7% |
| **+20¢** | 38933 | 27139 | 11794 (310) | 6 | $-13962.07 | -5.7% |
| **+10¢ (15¢ stop)** | 85144 | 84954 | 190 (118) | 4 | $-31273.16 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 12:02 | +10 stop | BNB | DOWN | 0.68 | open |  |
| 11-23 12:02 | +20 | BNB | DOWN | 0.68 | open |  |
| 11-23 12:02 | +15 | BNB | DOWN | 0.68 | open |  |
| 11-23 12:02 | +10 | BNB | DOWN | 0.68 | open |  |
| 11-23 12:02 | +5 | BNB | DOWN | 0.68 | 0.73 | 0.20 |
| 11-23 12:02 | +10 stop | XRP | DOWN | 0.60 | 0.71 | 0.78 |
| 11-23 12:02 | +5 | XRP | DOWN | 0.60 | 0.68 | 0.47 |
| 11-23 12:01 | +10 stop | ZEC | DOWN | 0.60 | 0.70 | 0.68 |
| 11-23 12:01 | +20 | ZEC | DOWN | 0.60 | open |  |
| 11-23 12:01 | +15 | ZEC | DOWN | 0.60 | open |  |
| 11-23 12:01 | +10 | ZEC | DOWN | 0.60 | 0.70 | 0.68 |
| 11-23 12:01 | +5 | ZEC | DOWN | 0.60 | 0.70 | 0.68 |
| 11-23 12:01 | +10 stop | XRP | DOWN | 0.57 | 0.68 | 0.76 |
| 11-23 12:01 | +20 | XRP | DOWN | 0.57 | 0.77 | 1.69 |
| 11-23 12:01 | +15 | XRP | DOWN | 0.59 | 0.77 | 1.50 |
| 11-23 12:01 | +10 | XRP | DOWN | 0.60 | 0.71 | 0.78 |
| 11-23 12:01 | +5 | XRP | DOWN | 0.60 | 0.68 | 0.47 |
| 11-23 12:01 | +10 stop | HYPE | DOWN | 0.62 | 0.46 | -1.95 |
| 11-23 12:01 | +20 | HYPE | DOWN | 0.62 | open |  |
| 11-23 12:01 | +15 | HYPE | DOWN | 0.62 | open |  |
| 11-23 12:01 | +10 | HYPE | DOWN | 0.62 | open |  |
| 11-23 12:01 | +5 | HYPE | DOWN | 0.62 | open |  |
| 11-23 12:01 | +10 stop | DOGE | DOWN | 0.60 | open |  |
| 11-23 12:01 | +20 | DOGE | DOWN | 0.60 | open |  |
| 11-23 12:01 | +15 | DOGE | DOWN | 0.60 | open |  |
| 11-23 12:01 | +10 | DOGE | DOWN | 0.60 | open |  |
| 11-23 12:01 | +5 | DOGE | DOWN | 0.60 | open |  |
| 11-23 12:01 | +10 stop | NEAR | DOWN | 0.56 | open |  |
| 11-23 12:01 | +20 | NEAR | DOWN | 0.56 | open |  |
| 11-23 12:01 | +15 | NEAR | DOWN | 0.56 | open |  |
| 11-23 12:01 | +10 | NEAR | DOWN | 0.56 | open |  |
| 11-23 12:01 | +5 | NEAR | DOWN | 0.56 | 0.63 | 0.34 |
| 11-23 12:01 | +10 stop | SOL | DOWN | 0.60 | open |  |
| 11-23 12:01 | +20 | SOL | DOWN | 0.60 | open |  |
| 11-23 12:01 | +15 | SOL | DOWN | 0.60 | open |  |
| 11-23 12:01 | +10 | SOL | DOWN | 0.60 | open |  |
| 11-23 12:01 | +5 | SOL | DOWN | 0.60 | open |  |
| 11-23 11:59 | +10 stop | XRP | UP | 0.56 | 0.09 | -4.99 |
| 11-23 11:59 | +20 | XRP | UP | 0.54 | no | -5.61 |
| 11-23 11:59 | +15 | XRP | UP | 0.50 | no | -5.18 |
