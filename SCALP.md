# Range-Scalp Bot

*Updated Mon Nov 02 13:32 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44922 | 39117 | 5805 (66) | 2 | $-12988.25 | -4.6% |
| **+10¢** | 33535 | 26809 | 6726 (87) | 4 | $-11853.22 | -5.6% |
| **+15¢** | 28044 | 20806 | 7238 (114) | 8 | $-10913.49 | -6.2% |
| **+20¢** | 24915 | 17338 | 7577 (149) | 9 | $-9640.28 | -6.2% |
| **+10¢ (15¢ stop)** | 54822 | 54735 | 87 (51) | 2 | $-20711.21 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 13:32 | +10 stop | ZEC | DOWN | 0.38 | 0.54 | 1.25 |
| 11-02 13:32 | +10 | ZEC | DOWN | 0.38 | 0.54 | 1.25 |
| 11-02 13:32 | +5 | NEAR | DOWN | 0.49 | 0.60 | 0.75 |
| 11-02 13:32 | +10 stop | BTC | DOWN | 0.54 | 0.65 | 0.76 |
| 11-02 13:32 | +10 | BTC | DOWN | 0.54 | 0.65 | 0.76 |
| 11-02 13:32 | +5 | BTC | DOWN | 0.53 | 0.65 | 0.86 |
| 11-02 13:32 | +10 stop | DOGE | DOWN | 0.42 | 0.63 | 1.75 |
| 11-02 13:32 | +10 | DOGE | DOWN | 0.42 | 0.63 | 1.75 |
| 11-02 13:32 | +5 | DOGE | DOWN | 0.42 | 0.63 | 1.75 |
| 11-02 13:32 | +5 | ZEC | DOWN | 0.58 | 0.65 | 0.36 |
| 11-02 13:32 | +10 stop | XRP | DOWN | 0.68 | 0.40 | -3.13 |
| 11-02 13:32 | +20 | XRP | DOWN | 0.69 | open |  |
| 11-02 13:32 | +15 | XRP | DOWN | 0.69 | open |  |
| 11-02 13:32 | +10 | XRP | DOWN | 0.69 | open |  |
| 11-02 13:32 | +5 | XRP | DOWN | 0.69 | open |  |
| 11-02 13:32 | +10 stop | HYPE | DOWN | 0.67 | 0.46 | -2.48 |
| 11-02 13:32 | +20 | HYPE | DOWN | 0.69 | open |  |
| 11-02 13:32 | +15 | HYPE | DOWN | 0.69 | open |  |
| 11-02 13:32 | +10 | HYPE | DOWN | 0.70 | open |  |
| 11-02 13:32 | +5 | HYPE | DOWN | 0.70 | open |  |
| 11-02 13:31 | +10 stop | ZEC | DOWN | 0.54 | 0.65 | 0.76 |
| 11-02 13:31 | +20 | ZEC | DOWN | 0.54 | open |  |
| 11-02 13:31 | +15 | ZEC | DOWN | 0.54 | open |  |
| 11-02 13:31 | +10 | ZEC | DOWN | 0.54 | 0.65 | 0.76 |
| 11-02 13:31 | +5 | ZEC | DOWN | 0.54 | 0.59 | 0.15 |
| 11-02 13:31 | +10 stop | NEAR | DOWN | 0.55 | open |  |
| 11-02 13:31 | +20 | NEAR | DOWN | 0.55 | open |  |
| 11-02 13:31 | +15 | NEAR | DOWN | 0.55 | open |  |
| 11-02 13:31 | +10 | NEAR | DOWN | 0.55 | open |  |
| 11-02 13:31 | +5 | NEAR | DOWN | 0.55 | 0.64 | 0.55 |
| 11-02 13:31 | +10 stop | BNB | DOWN | 0.65 | 0.76 | 0.81 |
| 11-02 13:31 | +20 | BNB | DOWN | 0.65 | open |  |
| 11-02 13:31 | +15 | BNB | DOWN | 0.65 | open |  |
| 11-02 13:31 | +10 | BNB | DOWN | 0.65 | 0.76 | 0.81 |
| 11-02 13:31 | +5 | BNB | DOWN | 0.65 | 0.72 | 0.39 |
| 11-02 13:31 | +10 stop | BTC | DOWN | 0.61 | 0.71 | 0.68 |
| 11-02 13:31 | +20 | BTC | DOWN | 0.61 | open |  |
| 11-02 13:31 | +15 | BTC | DOWN | 0.60 | open |  |
| 11-02 13:31 | +10 | BTC | DOWN | 0.60 | 0.71 | 0.78 |
| 11-02 13:31 | +5 | BTC | DOWN | 0.60 | 0.71 | 0.78 |
